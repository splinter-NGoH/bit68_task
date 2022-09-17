class CartSession:
    def __init__(self, request):
        self.request = request
    def cart_id(self):
        cart = self.request.session.session_key
        if not cart:
            cart = self.request.session.create()
        return cart
