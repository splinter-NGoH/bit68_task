from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from bit68_project.products.models import Product
from .cart_session_key import CartSession

from bit68_project.cart.models import CartItem, Cart
from .serializers import CartSerializer, CartItemListSerializer


class CartApiView(generics.GenericAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer

    def post(self, request, **kwargs):
        current_user = request.user
        slug = self.kwargs.get("slug")
        product = Product.objects.get(slug=slug) 
        if request.user.is_authenticated:
            is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user).exists()
            if is_cart_item_exists:
                cart_item = CartItem.objects.get(product=product, user=current_user,  pkid=item.pkid)
                for item in cart_item:
                    cur_item = CartItem.objects.get(product=product, pkid=item.pkid)
                    cur_item.quantity += 1
                    cur_item.save()
            else: 
                cart_item = CartItem.objects.create(
                    product = product,
                    quantity = 1,
                    user = current_user,
                )
                cart_item.save()
        else:
            
            try:
                cart = Cart.objects.get(cart_id=CartSession(request)) # get the cart using the cart_id present in the session
            except Cart.DoesNotExist:
                cart = Cart.objects.create(
                    cart_id = CartSession(request)
                )
            cart.save()

            is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
            if is_cart_item_exists:
                cart_item = CartItem.objects.filter(product=product, cart=cart)

            else:
                cart_item = CartItem.objects.create(
                    product = product,
                    quantity = 1,
                    cart = cart,
                )

            cart_item.save()

        cart_item = request.data
        # author = request.user
        # cart_item["author"] = author.pkid
        # cart_item["article"] = product.pkid
        # cart_item["cart"] = cart.pkid
        serializer = self.serializer_class(data=cart_item)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, **kwargs):
        current_user = request.user
        slug = self.kwargs.get("slug")
        product = Product.objects.get(slug=slug) #get the product
        if request.user.is_authenticated:
            is_cart_item_exists = CartItem.objects.filter(product=product, author=current_user).exists()
            if is_cart_item_exists:
                cart_item = CartItem.objects.get(product=product, author=current_user)
                cart_item.quantity += 1
                cart_item.save()
            else:
                cart_item = CartItem.objects.create(
                    product = product,
                    quantity = 1,
                    user = current_user,
                )
                cart_item.save()
        else:
            
            try:
                cart = Cart.objects.get(cart_id=CartSession(request)) # get the cart using the cart_id present in the session
            except Cart.DoesNotExist:
                cart = Cart.objects.create(
                    cart_id = CartSession(request)
                )
            cart.save()
            cart_item = CartItem.objects.filter(cart=cart, author=current_user)

            is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
            if is_cart_item_exists:
                cart_item = CartItem.objects.filter(product=product, cart=cart)

            else:
                cart_item = CartItem.objects.create(
                    product = product,
                    quantity = 1,
                    cart = cart,
                )

            cart_item.save()


            cart = Cart.objects.get(cart_id=CartSession(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        serializer = CartItemListSerializer(
            cart_items, many=True, context={"request": request}
        )
        return Response(
            {"num_cart_items": len(serializer.data), "cart_items": serializer.data,},
            status=status.HTTP_200_OK,
        )


# class CartDeleteUpdateApiView(generics.GenericAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = CommentSerializer

#     def put(self, request, slug, id):
#         try:
#             comment_to_update = Comment.objects.get(id=id)
#         except Comment.DoesNotExist:
#             raise NotFound("Comment does not exist")

#         data = request.data
#         serializer = self.serializer_class(comment_to_update, data=data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         response = {
#             "message": "Comment updated successfully",
#             "comment": serializer.data,
#         }
#         return Response(response, status=status.HTTP_200_OK)

#     def delete(self, request, slug, id):
#         try:
#             comment_to_delete = Comment.objects.get(id=id)
#         except Comment.DoesNotExist:
#             raise NotFound("Comment does not exist")

#         comment_to_delete.delete()
#         response = {"message": "Comment deleted successfully!"}
#         return Response(response, status=status.HTTP_200_OK)
