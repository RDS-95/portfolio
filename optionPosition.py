class optionPosition:
    def __init__(self):
        self.options = []
        self.graph_max = 10
        self.final_prices = np.arange(0, 200, 0.5)
        self.payouts = np.zeros_like(self.final_prices)
    
    def update_graph_max(self, strike_price):
        """
        update_graph_max keeps track of the required plotting range.
        """ 
        if strike_price > self.graph_max - 50:
            self.graph_max = strike_price + 50
    
    def call_payout(self, strike_price, premium, quantity):
        """
        Calculate the payout of a standard vanilla call option.
        strike_price: The strike/exercise price of the option
        premium: The premium paid for the contract
        quantity: The number of contracts purchased. Can take negative values if writing contracts.
        """ 
        return quantity * (np.where(self.final_prices > strike_price, self.final_prices - strike_price, 0) - premium)
    
    def put_payout(self, strike_price, premium, quantity=1):
        """
        Calculate the payout of a standard vanilla put option.
        strike_price: The strike/exercise price of the option
        premium: The premium paid for the contract
        quantity: The number of contracts purchased. Can take negative values if writing contracts.
        """ 
        return quantity * (np.where(self.final_prices < strike_price, strike_price - self.final_prices, 0) - premium)
    
            
    def add_call_option(self, strike_price, premium, quantity=1):
        """
        Adds a call option to the current position and updates the payoffs accordingly
        strike_price: The strike/exercise price of the option
        premium: The premium paid for the contract
        quantity: The number of contracts purchased. Can take negative values if writing contracts.
        """ 
        self.update_graph_max(strike_price)
        option = {
            'type': 'Call',
            'strike_price': strike_price,
            'premium': premium,
            'quantity': quantity
        }
        self.options.append(option)
        self.payouts = np.add(self.payouts, self.call_payout(strike_price, premium, quantity))


    def add_put_option(self, strike_price, premium, quantity=1):
        """
        Adds a put option to the current position and updates the payoffs accordingly
        strike_price: The strike/exercise price of the option
        premium: The premium paid for the contract
        quantity: The number of contracts purchased. Can take negative values if writing contracts.
        """ 
        self.update_graph_max(strike_price)
        option = {
            'type': 'Put',
            'strike_price': strike_price,
            'premium': premium,
            'quantity': quantity
        }
        self.options.append(option)
        self.payouts = np.add(self.payouts, self.put_payout(strike_price, premium, quantity))


    def show_position(self):
        """
        Prompts a display of the current options held, summarizing the position.
        """ 
        if len(self.options) == 0:
            print("Current position is closed.")
            return

        print("Current Position:")
        for index, option in enumerate(self.options, start=1):
            option_type = option['type']
            strike_price = option['strike_price']
            premium = option['premium']
            quantity = option['quantity']
            print(f"Option {index}: {option_type} - Strike Price: {strike_price}, Premium: {premium}, Quantity: {quantity}")
    
    def find_breakeven_points(self):
        """
        find_breakeven_points gets the final asset prices where the holder of the position is breaking even.
        """ 
        
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
        plt.figure(figsize=(10, 6))
        plt.plot(self.final_prices, self.payouts, label='Position Payoff')
        plt.xlabel('Final Asset Prices')
        plt.ylabel('Payoff')
        plt.title('Combined Position Payoff')
        plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
        
        # Add and annotate breakeven points on the plot.
        breakeven_points = self.find_breakeven_points()
        for point in breakeven_points:
            plt.scatter(self.final_prices[point], self.payouts[point], color='green', s=50, label='Breakeven Point')
            plt.annotate(f'{self.final_prices[point]}', (self.final_prices[point], self.payouts[point]),
                         textcoords="offset points", xytext=(5, 5), ha='center')

        # Prevent duplicate labels appearing in the legend.
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        
        plt.xlim(0, self.graph_max)
        plt.grid(True)
        plt.show()
