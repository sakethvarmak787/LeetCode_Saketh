class Solution:
    def shoppingOffers(self, price, special, needs):
        
        # memo will store results for already solved states
        # key = tuple(needs), value = minimum cost
        memo = {}
        
        def dfs(current_needs):
            
            # Convert list to tuple so it can be used as dictionary key
            needs_tuple = tuple(current_needs)
            
            # -----------------------------
            # Step 1: Check if already solved
            # -----------------------------
            if needs_tuple in memo:
                # We have already computed this state before
                return memo[needs_tuple]
            
            # -----------------------------
            # Step 2: Buy everything directly
            # -----------------------------
            cost = 0
            for i in range(len(price)):
                cost += current_needs[i] * price[i]
            
            # Example dry run:
            # current_needs = [3,2]
            # cost = 3*2 + 2*5 = 16
            
            min_cost = cost
            
            # -----------------------------
            # Step 3: Try every special offer
            # -----------------------------
            for offer in special:
                
                new_needs = []
                valid = True
                
                for i in range(len(price)):
                    # If offer exceeds needs → cannot use
                    if offer[i] > current_needs[i]:
                        valid = False
                        break
                    new_needs.append(current_needs[i] - offer[i])
                
                if valid:
                    # Apply offer and go deeper
                    
                    offer_price = offer[-1]
                    
                    # Example parallel dry run:
                    # current_needs = [3,2]
                    # offer = [1,2,10]
                    # new_needs = [2,0]
                    # total_cost = 10 + dfs([2,0])
                    
                    total_cost = offer_price + dfs(new_needs)
                    
                    min_cost = min(min_cost, total_cost)
            
            # -----------------------------
            # Step 4: Store result in memo
            # -----------------------------
            memo[needs_tuple] = min_cost
            
            return min_cost
        
        return dfs(needs)