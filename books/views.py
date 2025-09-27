from django.http import JsonResponse
from django.shortcuts import render
from .models import Book

# Create your views here.

def get_title(request):
    # リクエストがGETであることを確認
    if request.method == 'GET':
        # クエリパラメータから 'title' を取得
        title = request.GET.get('title', None)
        
        # 'title' が提供されているか確認
        if not title:
            return JsonResponse({'error': 'Title parameter is required.'}, status=400)
        
        # データベースでタイトルを検索
        try:
            book = Book.objects.get(title=title)
            return JsonResponse({'title': book.title}, status=200)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book with the given title does not exist.'}, status=404)
    
    # GET以外のリクエストはエラーを返す
    return JsonResponse({'error': 'Invalid request method.'}, status=405)
