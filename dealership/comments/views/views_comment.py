# from django.shortcuts import render, redirect, get_object_or_404
# from django.views import View
# from offer.models import Offer
# from comments.forms import CommentForm
# from comments.repositories.comment_repository import CommentRepository
# repo_comment = CommentRepository()

# # Create your views here.
# class CommentCreate(View):   
#     def post(self, request, id):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             offer = get_object_or_404(Offer, id=id)
#             # Crear el comentario
#             repo_comment.create(
#                 name=form.cleaned_data['name'],
#                 offer=offer,
#                 profile=request.user
#             )
#             return redirect('DetailOffers', id=id)
#         else:
#             return render(
#                 request,
#                 'offer/templates/offers/list.html',
#                 dict(
#                     form=form
#                 )
#             )   