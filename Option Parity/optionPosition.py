import numpy as np
import matplotlib.pyplot as plt


class OptionPosition:
    def __init__(self):
        self.options = []
        self.graph_max = 10  # arbitrary
        self.final_prices = np.arange(0, 200, 0.5)
        self.payouts = np.zeros_like(self.final_prices)
        self.fig, self.ax = plt.subplots(figsize=(10, 4))
    
    def update_graph_max(self, strike_price):
        """
        update_graph_max keeps track of the required plotting range.
        """ 
        if strike_price > self.graph_max - 50:
            self.graph_max = strike_price + 50
    
    def call_payout(self, strike_price, premium):
        return np.where(self.final_prices > strike_price, self.final_prices - strike_price, 0) - premium
    
    def put_payout(self, strike_price, premium):
        return np.where(self.final_prices < strike_price, strike_price - self.final_prices, 0) - premium

    def add_option(self, strike_price, premium, option_type, position_type):
        """
        Adds a call/put option to the current position and updates the payoffs accordingly
        strike_price: The strike/exercise price of the option
        premium: The premium paid for the contract
        """
        self.update_graph_max(strike_price)
        self._validate_option_parameters(option_type, position_type)
        self._append_option(option_type, strike_price, premium)

        if option_type == "Call":
            if position_type == "Long":
                self.payouts = np.add(self.payouts, self.call_payout(strike_price, premium))
            elif position_type == "Short":
                self.payouts = np.add(self.payouts, -self.call_payout(strike_price, premium))
        else:  # option_type == "Put"
            if position_type == "Long":
                self.payouts = np.add(self.payouts, self.put_payout(strike_price, premium))
            elif position_type == "Short":
                self.payouts = np.add(self.payouts, -self.put_payout(strike_price, premium))

    def _validate_option_parameters(self, option_type, position_type):
        if option_type not in ("Call", "Put"):
            raise ValueError(f'Invalid Option Type: "{option_type}". Accepted Values: "Call", "Put"')
        if position_type not in ("Long", "Short"):
            raise ValueError(f'Invalid Position Type: "{position_type}". Accepted Values: "Long", "Short"')

    def _append_option(self, option_type, strike_price, premium):
        option = {'type': option_type, 'strike_price': strike_price, 'premium': premium}
        self.options.append(option)

    def show_position(self):
        if len(self.options) == 0:
            print("Current position is closed.")
            return

        print("Current Position:")
        for index, option in enumerate(self.options, start=1):
            option_type = option['type']
            strike_price = option['strike_price']
            premium = option['premium']
            print(f"Option {index}: {option_type} - Strike Price: {strike_price}, "
                  f"Premium: {premium}")

    def find_breakeven_points(self):
        # Use change of signs in payouts to find where the crossings are.
        crossings = np.where(np.diff(np.sign(self.payouts)))[0]
        
        # Filter out duplicate crossings, keeping only the first occurrence
        unique_crossings = []
        prev_index = -1
        for crossing in crossings:
            if crossing != prev_index + 1:
                unique_crossings.append(crossing)
            prev_index = crossing

        # Convert indices to integers
        unique_crossings = np.array(unique_crossings, dtype=int)
        return unique_crossings
    
    def parity_graph(self):
        """
        parity_graph creates a diagram summarizing payout at expiry based on the current position.
        It takes into account all options currently held/written.
        """
        self.ax.clear()

        self.ax.plot(self.final_prices, self.payouts, label='Position Payoff')
        self.ax.set_xlabel('Final Asset Prices')
        self.ax.set_ylabel('Payoff')
        self.ax.set_title('Combined Position Payoff')
        self.ax.axhline(0, color='black', linestyle='--', linewidth=0.8)
        
        # Add and annotate breakeven points on the plot.
        breakeven_points = self.find_breakeven_points()
        for point in breakeven_points:
            self.ax.scatter(self.final_prices[point], self.payouts[point], color='green', s=50, label='Breakeven Point')
            self.ax.annotate(f'{self.final_prices[point]}', (self.final_prices[point], self.payouts[point]),
                             textcoords="offset points", xytext=(5, 5), ha='center')

        # Prevent duplicate labels appearing in the legend.
        handles, labels = self.ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        self.ax.legend(by_label.values(), by_label.keys())

        self.ax.set_xlim(0, self.graph_max)
        plt.tight_layout()
        plt.grid(True)
        plt.show()
