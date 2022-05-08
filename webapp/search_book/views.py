from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView
from .forms import SearchForm
from . import SEARCH_BOOKAPP_URLS_LABEL
import json
import requests
from config import settings

API_ID = settings.RAKUTEN_API_KYE
SEARCH_URL = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?fromat=json&applicationId=' + API_ID

# APIにリクエストを送り, json形式で結果を受け取り, リストにして返す関数
def get_api_data(params):
    api = requests.get(SEARCH_URL, params=params).text
    result = json.loads(api)
    items = result['Items']
    return items

# ルーティングでsearch_book/indexが指定された場合
class IndexView(LoginRequiredMixin, View):
    template_name = "%s/index.html" % SEARCH_BOOKAPP_URLS_LABEL

    # getでリクエストを受け取った場合
    def get(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        return render(request, "%s/index.html" % SEARCH_BOOKAPP_URLS_LABEL, {'form':form})

    # postでリクエストを受け取った場合
    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        # バリデーションを行う
        if form.is_valid():
            # フォームから値を取得
            keyword = form.cleaned_data['title']
            params = {
                'title': keyword,
                'hits': 30,
            }
            items = get_api_data(params)
            book_data = []
            for content in items:
                # jsonデータのうちItemだけ取り出す
                item = content['Item']
                # Itemから必要な書籍情報を取り出す
                title = item['title']
                image = item['largeImageUrl']
                isbn = item['isbn']
                # バックエンドで扱えるように辞書にする
                query = {
                    'title': title,
                    'image': image,
                    'isbn': isbn
                }
                # 辞書をリストに格納する
                book_data.append(query)
            
            return render(request, "%s/search_result.html" % SEARCH_BOOKAPP_URLS_LABEL,{
                'book_data': book_data, #検索結果リスト
                'keyword': keyword #検索ワード
            })
        
        # データが不正だったらフォームを再描画する
        return render(request, "%s/index.html" % SEARCH_BOOKAPP_URLS_LABEL, {'form':form})

# ルーティングでsearch_book/indexが指定された場合
class DetailView(LoginRequiredMixin, View):
    template_name = "%s/detail.html" % SEARCH_BOOKAPP_URLS_LABEL

    # getでリクエストを受け取った場合
    def get(self, request, *args, **kwargs):
        # リクエストからisbnを取り出す
        isbn = self.kwargs['isbn']
        params = {
            'isbn':isbn
        }

        # isbnよりAPIで検索実行
        items = get_api_data(params)

        # 検索結果から書籍情報を取り出す
        items = items[0]
        item = items['Item']
        # 書籍情報よりひとつずつ変数へ詰め込む
        title = item['title']
        image = item['largeImageUrl']
        author = item['author']
        itemPrice = item['itemPrice']
        salesDate = item['salesDate']
        publisherName = item['publisherName']
        size = item['size']
        isbn = item['isbn']
        itemCaption = item['itemCaption']
        itemUrl = item['itemUrl']
        reviewAverage = item['reviewAverage']
        reviewCount = item['reviewCount']

        # バックエンドで扱えるように辞書に変換
        book_data = {
            'title': title,
            'image': image,
            'author': author,
            'itemPrice': itemPrice,
            'salesDate': salesDate,
            'publisherName': publisherName,
            'size': size,
            'isbn': isbn,
            'itemCaption': itemCaption,
            'itemUrl': itemUrl,
            'reviewAverage': reviewAverage,
            'reviewCount': reviewCount,
            'average': float(reviewAverage) * 20,
            'keyword': self.kwargs['keyword'],
        }

        return render(request, "%s/detail.html" % SEARCH_BOOKAPP_URLS_LABEL, {'book_data':book_data})