# my_first_web_app
いつぞやにつくったdjangoのWebアプリがあるが, 一連の作り方を忘れたので学習をし直す  
*本来ならcmderは不要なものだが, 他環境で同じ設定のcmderを利用したいのでおいておく  

# 1. pythonの仮想環境を作る

<details>
<summary>pythonの仮想環境を作る</summary>

## 1-1. pyenvとvenvで仮想環境構築
一応, 仮想環境で作成して他に移せるようにしておく（やり方の復習の意味合いを込めて）  
pyenvでバージョン管理, 今回は新しめのversionにしようと思うので, 3.9.0にする  
venvで今回使用するパケージを突っ込んでいく  

1. [windowsでpyenvを使う方法の参考サイト](https://www.3ryu-engineer.work/windows-pyenv/)
2. `pyenv versions`で現在のversin確認, 3.9.0がなかったら`pyenv install 3.9.0`でInstall
3. `pyenv shell 3.9.0`で切り替え
4. 備考：システム全体のversionは`pyenv global hoge`で指定可能
5. 切り替えた環境, かつ, 対象PJディレクトリにおいて`python -m venv .venv`を実行し, 仮想環境作成
6. 作成した仮想環境をActivateする：`source .venv/Scripts/activate`（cmdなら`.venv\Scripts\activate.bat`）
7. Activateできていれば, (.venv)的なものがターミナルやらCMDやらにでてくるはず（使ってるものによって変わる）
8. 必要なライブラリをpip installすればOK
9. 終了するときは`diactivate`

## 1-2. 仮想環境のコピー
.venvの内容をコピーするにはパッケージの一覧を共有する  

1. `python -m pip freeze > requirements.txt`を実行
2. コピー側で`python -m pip install -r requirements.txt`を実行

## 1-3. 仮想環境情報のディレクトリはgitに上げるものじゃないので対象から外す
1. `vim .gitignore`でファイル作成
2. .gitignoreに対象ファイルやディレクトリを記載, 今回は`/.venv/`を記載

</details>

# 2. djangoプロジェクトの始め方

<details>
<summary>djangoプロジェクトの始め方</summary>

## 2-1. djangoでpjを作成する
1. `django-admin startproject hoge`
2. `cd hoge`
3. `python manage.py runserver`
4. これだけで作成完了, めっちゃ簡単

## 2-2. gitへの初回push方法
### 2-2-1. 何にもないrepositoryの場合
1. READMEをつくる：`echo "# my_first_web_app" >> README.md`
2. `git init`
3. `git add README.md`
4. `git commit -m "first commit"`
5. ブランチをmaster以外にする場合：`git branch -M main`
6. `git remote add origin https://github.com/naoki0130/my_first_web_app.git`
7. `git push -u origin ブランチ名`

### 2-2-2. すでにrepositoryにある場合
1. `git remote add origin https://github.com/naoki0130/my_first_web_app.git`
2. `git branch -M ブランチ名`
3. `git push -u origin ブランチ名`

### 2-2-3. Gitでユーザー名とメールアドレスを設定する方法
1. git config --global user.name "ユーザー名"
2. git config --global user.email メールアドレス
3. pjごとにしたい場合は, globalの部分をlocalにすればOK

</details>

# 3. djangoで開発

<details>
<summary>djangoで開発</summary>

## 3.1 djangoでアプリを作成する
1. `python manage.py startapp webapp`
2. ディレクトリができているはず, htmlを配置する場合は`templates`ディレクトリと`urls.py`を作成する

## 3-2. djangoで開発：ざっくり概要
1. setting.pyにおいて, ALLOWED_HOSTSを`*`にする
2. LANGUAGE_CODEを`ja`にする
3. TIME_ZONEを`Asia/Tokyo`にする
4. アプリを追加したらINSTALLED_APPSに追記する
5. MW(whitenoiseやcloudynaryなど)を追加した際はMIDDLEWAREに追記する
6. アプリでhtmlを読み込ませるためにviewにclassを作成(中身はTemplateViewを継承して, template_nameにhtmlのファイル名を記載する)
7. アプリを追加した場合は(かつhtmlを見せるアプリの場合は), pjディレクトリにおけるurls.pyに`include(アプリ名.urls)`を追記する
8. アプリ側のurls.pyにおいても.viewsをimportして`class名.as_view()`と追記する
9. これで大体OK
10. そのうちwhitenoiseで静的ファイルを管理する, コマンドは`python manage.py collectstatic`：[参考サイト](`whitenoise.middleware.WhiteNoiseMiddleware`,)

## 3-3. djangoにおけるそれぞれのpyファイルの役割
pj側とapp側でそれぞれ示す  

### 3-3-1. PJ側
- setting.py：設定もろもろを記載する
- urls.py：PJの大本となるURLを設定する, その下のアプリのURLを紐づけて扱える

### 3-3-2. app側
- models.py：DBに突っ込むようなデータ情報をクラスで表現する, DBのやり取りをこのファイルの定義から勝手にやってくれるためSQLを書く必要なし
- urls.py：クライアントからのリクエストをルーティングしてくれてviewsのなんの関数やクラスを見に行くか指定する, アプリのURLを設定する, URL変更のメンテを楽にするためにnameを指定することを推奨
- views.py：urls.pyから呼ばれて必要に応じてDBとのやり取りをおこないhtmlを表示させる

## 3-4. templateの管理について
- templatesはPJ直下で管理する  
- templates配下にアプリごとのディレクトリを切り, base.html以外を配置する  
- アプリごとのurls.pyにはapp_nameをつける(htmlで`urls hoge:fuga`的な記述を可能にするため)
- アプリごとの__init__.pyにtemplates配下のアプリディレクトリを記述しておく

<details>
<summary>templatesの例</summary>

### PJ urls.py
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("webapp.urls")),
]
```

### webapp urls.py
```
from unicodedata import name
from django.urls import path, include
from webapp.views import *

app_name = 'webapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('blog/', include('webapp.blog.urls', namespace='blog'), name='blog'),
]
```

### blog urls.py
```
from django.urls import path
from .views import BlogView

app_name = 'blog'
urlpatterns = [
    path('blogpage/', BlogView.as_view(), name='blogpage'),
]
```

### templates
```
<div id = "navbar">

    <div id = "navbar_menue">
        <a href="{% url 'webapp:index' %}">home</a>
        <a href="{% url 'webapp:about' %}">about</a>
        <a href="{% url 'webapp:blog:blogpage' %}">blog</a>
    </div>

    <div id="navbar_now" >
        <a>{% now 'Y-m-d H:i:s' %}</a>
    </div>

</div>

```

</details>

## 3-5. DBの設定について
- 今回は今後使っていくことも踏まえて学習目的でpostgresqlを利用する  
- とはいいつつもmodelでよしなにやるから気にしなくていいが

### 3-5-1. pip installとsettings.pyの設定変更
```
pip install dj-database-url
pip install python-dotenv

load_dotenv(find_dotenv())
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600),
}
```

### 3-5-2. postgresqlの設定
```
pip install psycopg2-binary

psql -U postgres

\password postgres

CREATE DATABASE my_first_web_app_db;

\q
```

### 3-5-3. viファイル設定
```
.envに追記

DATABASE_URL=postgres://postgres:pass@localhost/my_first_web_app_db
```

### 3-5-4. superuser追加
```
python manage.py createsuperuser
```

### 3-5-5. herokuでdbの設定
```
python manage.py  migrate

python manage.py createsuperuser
```

### 3-5-6. models.pyの内容をdbに反映させる
```
python manage.py makemigrations hoge

python manage.py makemigrations hoge/fuga

python manage.py migrate
```

### 3-5-7. アプリごとでadmin.pyに追加したmodelを追記する（テーブル追加）
```
@admin.register(models.hoge)
class HogeAdmin(admin.ModelAdmin):
  pass
```

</details>


# 4. herokuでデプロイ

<details>
<summary>herokuでデプロイ</summary>

## 4.1 herokuでデプロイするには
なにやらGUIでデプロイができないので, CLIでの方法を記す(GUIだとめちゃくちゃ簡単)  
デプロイの詳細は[このサイトでOK](https://devcenter.heroku.com/ja/articles/git)  

## 4-2. なんか躓いたこと
pythonのversionによってデプロイできない  
が, winのpyenvでは対象versionをInstallできないジレンマ  
とりあえず, pyenv側は3.10.0a1でruntime.txtにheroku対応の3.10.2を記載でうまくいった  
### 4-2-1. 追記
procfileの位置が悪くてうまく起動できない事象に遭遇  
ちゃんとPJ配下に作成する  

### 4-2-2. 追記２
結局の原因はPJがネストしすぎ  
PJ直下でvenv環境つくって諸々の手順を踏めばOK  

## 4-3. 最初にすること
0. requirements.txtとruntime.txtがないとバグる可能性大
1. `heroku login`
2. 下記の新規か既存の設定をする
3. deployする

### 4-3-1. 新規
1. `heroku create -a hogeapp`
2. アプリと合ってるか確認：`git remote -v`

### 4-3-2. 既存
1. `heroku git:remote -a hogeapp`

### 4-3-3. herokuリモート名の変更
1. `git remote rename hoge hoge-rename`

### 4-3-4. コードのデプロイ
1. `git push heroku main`

</details>

# 5. その他
## 5-1. cmderの設定
cmderが使い慣れているので設定する  
参考サイトは[ここである](https://qiita.com/thrzn41/items/7dd3b1ec5e50bae9f03b)  

## 5-2. vscodeの設定について
自宅PCの馴染んだ環境を再現するために設定情報を共有  
といってもcmderくらいだが  

<details>
<summary>setting</summary>

```
{
  "workbench.colorTheme": "Monokai Pro",
  "workbench.colorCustomizations": {
    "sideBar.background": "#141414",
    "activityBar.background": "#141414",
    "editor.background": "#181818",
    "panel.background": "#181818",
    "terminal.background": "#181818",
    "editorGroupHeader.tabsBackground": "#181818",
    "tab.inactiveBackground": "#181818",
    "editorGutter.background": "#181818"
  },
  "bracket-pair-colorizer-2.colorMode": "Independent",
  "bracket-pair-colorizer-2.colors": ["White", "Gold", "Orchid"],
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.linting.lintOnSave": true,
  "python.linting.flake8Args": ["--max-line-length=100"],
  "editor.formatOnSave": true,
  "editor.formatOnType": true,
  "python.formatting.provider": "autopep8",
  "python.formatting.autopep8Args": [
    "--max-line-length=100"
    //"--aggressive", "--aggressive",
  ],
  "editor.renderWhitespace": "all",
  "editor.fontSize": 14,
  "cSpell.userWords": [
    "cloudinary",
    "fuga",
    "hoge",
    "imshow",
    "pyplot",
    "pyxel",
    "scipy",
    "xlabel",
    "ylabel"
  ],
  "[html]": {
    "editor.defaultFormatter": "vscode.html-language-features"
  },
  "ruby.format": "rubocop",
  "ruby.codeCompletion": "rcodetools",
  "ruby.intellisense": "rubyLocate",
  "ruby.lint": {
    "ruby.codeCompletion": "rcodetools",
    "ruby.format": "rubocop",
    "ruby.intellisense": "rubyLocate",
    "ruby.lint": {
      "reek": true,
      "rubocop": true,
      "ruby": true, //Runs ruby -wc
      "fasterer": true,
      "debride": true,
      "ruby-lint": true
    },
    "ruby.locate": {
      "exclude": "{**/@(test|spec|tmp|.*),**/@(test|spec|tmp|.*)/**,**/*_spec.rb}",
      "include": "**/*.rb"
    }
  },

  // ---------- Language ----------

    "[tex]": {
        // スニペット補完中にも補完を使えるようにする
        "editor.suggest.snippetsPreventQuickSuggestions": false,
        // インデント幅を2にする
        "editor.tabSize": 2
    },

    "[latex]": {
        // スニペット補完中にも補完を使えるようにする
        "editor.suggest.snippetsPreventQuickSuggestions": false,
        // インデント幅を2にする
        "editor.tabSize": 2
    },

    "[bibtex]": {
        // インデント幅を2にする
        "editor.tabSize": 2
    },


    // ---------- LaTeX Workshop ----------

    // 使用パッケージのコマンドや環境の補完を有効にする
    "latex-workshop.intellisense.package.enabled": true,

    // 生成ファイルを削除するときに対象とするファイル
    // デフォルト値に "*.synctex.gz" を追加
    "latex-workshop.latex.clean.fileTypes": [
        "*.aux",
        "*.bbl",
        "*.blg",
        "*.idx",
        "*.ind",
        "*.lof",
        "*.lot",
        "*.out",
        "*.toc",
        "*.acn",
        "*.acr",
        "*.alg",
        "*.glg",
        "*.glo",
        "*.gls",
        "*.ist",
        "*.fls",
        "*.log",
        "*.fdb_latexmk",
        "*.snm",
        "*.nav",
        "*.dvi",
        "*.synctex.gz"
    ],

    // 生成ファイルを "out" ディレクトリに吐き出す
    "latex-workshop.latex.outDir": "out",

    // ビルドのレシピ
    "latex-workshop.latex.recipes": [
        {
            "name": "latexmk",
            "tools": [
                "latexmk"
            ]
        },
    ],

    // ビルドのレシピに使われるパーツ
    "latex-workshop.latex.tools": [
        {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
                "-silent",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ],
        },
    ],
    "latex-workshop.view.pdf.viewer": "tab",
    "workbench.startupEditor": "newUntitledFile",
    "vsicons.dontShowNewVersionMessage": true,
    "editor.suggestSelection": "first",
    "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
    "files.exclude": {
      "**/.classpath": true,
      "**/.project": true,
      "**/.settings": true,
      "**/.factorypath": true
    },

    	
    "terminal.integrated.shell.windows": "cmd.exe",
    
    "terminal.integrated.shellArgs.windows": [
      "/k", "C:\\Users\\key12\\cmder-20210331T003603Z-001\\cmder\\vendor\\init.bat"
    ],
    "git.ignoreMissingGitWarning": true,
    "terminal.integrated.fontFamily": "Source Code Pro for Powerline",
    "workbench.editorAssociations": {
      "*.ipynb": "jupyter-notebook",
      "*.xlsx": "default",
      "*.exe": "default"
    },
    "notebook.cellToolbarLocation": {
      "default": "right",
      "jupyter-notebook": "left"
    },
    "files.autoSave": "afterDelay",
    "notebook.consolidatedRunButton": true,
    "bracket-pair-colorizer-2.depreciation-notice": false,
    "bracketPairColorizer.depreciation-notice": false,

    //"terminal.integrated.shell.windows": "C:\\Users\\key12\\cmder-20210331T003603Z-001\\cmder\\vendor\\init.bat",

}
```
</details>