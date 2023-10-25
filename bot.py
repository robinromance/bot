# questions you can ask my bot
# 1, what product do you have
# 2, hi
# 3, about you
# 4, exit
# 5, tell me about + product name
# 6, show me my cart

import data_base
cart = []


def greet():
    return "Welcome to the Virtual Store! How can I assist you today?"


# def availability_checker():
#     for avail in range(len(data_base.products)):
#         if data_base.products[avail]['availability'] == 'In stock':
#             return True
#         else:
#             return False


# for find product
def product_searcher(n):
    for e in range(len(data_base.products)):
        hint = 'tell me about ' + data_base.products[e]['name'].lower()
        if n == hint:
            name = data_base.products[e]['name']
            price = data_base.products[e]['price']
            description = data_base.products[e]['description']
            availability = data_base.products[e]['availability']
            print(f"\t Name : {name} \n\t Description : {description} \n\t Price : ₹{price}"
                  f" \n\t Availability : {availability}")
            if availability == "In stock":
                # to ADD items in cart
                add_to_cart = input("\n\t If you like to 'Add' this product in your 'Cart' press 1 else 2 :")
                if add_to_cart == '1':
                    cart.append(data_base.products[e]['name'])
                    break
            else:
                print(f"\n\t 'X' Item not available if is there will inform you Tnx!")
    else:
        return "Product not found"


def main():
    print(greet())
    flag = True

    # loop iteration
    while flag:
        print('\n')
        print('***'.ljust(27, '-') + '***'.rjust(27, '-'))
        user = input('Ask me something ... :').lower()
        print('Bot :')

        # place order
        def display(item):
            payable_amount = 0
            for k in item:
                for l in range(len(data_base.products)):
                    if k == data_base.products[l]['name']:
                        price = data_base.products[l]['price']
                        payable_amount += price
            print(f"The payable amount is '{payable_amount}'.")

        # display our product list
        if user == 'what product do you have':
            for i in range(len(data_base.products)):
                re = data_base.products[i]['name']
                print(f"\t\t{i}, {re}")
        elif user == "hi":
            print("\t hi, there!!".title())
        elif user == 'about you':
            print('\t I am a virtual assistant bot !'.title())
        elif user == 'show me my cart':
            if not cart:
                print('Your cart is Empty !')
            else:
                print('\t Your Cart Items :')
                for element in cart:
                    print('\t\t ', element)
                payment = input("\t If you want to continue press 'y' else 'n' :").lower()
                if payment == 'y':
                    display(cart)
                    confirm = input("\t If you want to place your order press 'y' else 'n' :").lower()
                    if confirm == 'y':
                        cart.clear()
                        print("\t\t Successfully placed your order!".title())
        elif user == 'exit':
            print("\t Thank you for your time, Bye !!")
            flag = False
        else:
            # check each product in our store
            for i in range(len(data_base.products)):
                if user == 'tell me about ' + data_base.products[i]['name'].lower():
                    product_searcher(user)
                    break
            else:
                # if it has nothing match with our product error message
                print('Please ask me a valid question!')


if __name__ == "__main__":
    main()
