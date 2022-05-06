from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm
from . import ACCOUNTAPP_URLS_LABEL

# ルーティングでaccount/signupが指定された場合
class SignUpView(CreateView):
    template_name = "%s/signup.html" % ACCOUNTAPP_URLS_LABEL

    form_class = SignUpForm

    # signup後に移動する先
    success_url = reverse_lazy('webapp:index')

    def form_valid(self, form):
        if self.request.POST['next'] == 'back':

            return render(self.request, "%s/signup.html" % ACCOUNTAPP_URLS_LABEL, {'form': form})

        elif self.request.POST['next'] == 'confirm':

            return render(self.request, "%s/signup_confirm.html" % ACCOUNTAPP_URLS_LABEL, {'form': form})

        elif self.request.POST['next'] == 'regist':
            form.save()
            # 認証
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            # ログイン
            login(self.request, user)
            return redirect(reverse_lazy('webapp:index'))
        else:
            # 通常このルートは通らない
            return redirect(reverse_lazy('webapp:index'))
