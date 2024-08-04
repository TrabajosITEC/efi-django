from django.shortcuts import render, redirect
from django.views import View
from comments.repositories.comment_repository import CommentRepository
repo_comment = CommentRepository()

class CommentDelete(View):
    def get(self,request,id):
        comment = repo_comment.get_by_id(id=id)
        repo_comment.delete(comment=comment)
        return redirect('DetailOffers', id=comment.offer.id)