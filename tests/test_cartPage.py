from cartPage import cartPage
from basePage import basePage
from storePage import storePage
from cartPage import cartPage

class Test_cartPage():
    def test_cart_values(self, browser): 
        
        ## Test Case: 3 ##
            # 1. Buy 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear
            # 2. Got to cart page
            # 3. Verify the subtotal for each product is correct 
            # 4. Verify the price for each product
            # 5. Verify that total = sum(sub totals)

        page = basePage(browser)
        page.load()
        page.click_StorePage()

        shop = storePage(browser)

        ## Buy 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear
        # Stuffed Frog button
        shop.buy_Frog_Btn(2)
            
        # Fluffy Bunny button
        shop.buy_Bunny_Btn(5)

        # Valentine Bear button 
        shop.buy_VBear_btn(3)

        ## Navigate to Cart
        page.click_CartPage()

        cart = cartPage(browser)

        # Verify the subtotal for each product is correct 
        frog_subTotal = cart.get_cell_text(3)
        bunny_subTotal = cart.get_cell_text(8) 
        vbear_subTotal = cart.get_cell_text(13)

        assert "$21.98" == frog_subTotal
        assert "$49.95" == bunny_subTotal
        assert "$44.97" == vbear_subTotal

        # Verify price for each prodict 
        frog_price = cart.get_cell_text(1)
        bunny_price = cart.get_cell_text(6)
        vbear_price = cart.get_cell_text(11)

        assert "$10.99" == frog_price #$10.99
        assert "$9.99" == bunny_price
        assert "$14.99" == vbear_price

        # Verify that total = sum(sub totals)
        # convert sub total text to float 
        frog_subTotalNum = cart.text_to_Float(frog_subTotal,  '$', '')
        bunny_subTotalNum = cart.text_to_Float(bunny_subTotal, '$', '')
        vbear_subTotalNum = cart.text_to_Float(vbear_subTotal, '$', '')

        # extract total as float 
        CartTotal = cart.get_total()
        totalNum = cart.text_to_Float(CartTotal, 'Total: ', '')

        # verify the total = the sum of the sub totals 
        assert totalNum == frog_subTotalNum + bunny_subTotalNum + vbear_subTotalNum