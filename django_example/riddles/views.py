from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Riddle, Option


class IndexView(View):
    def get(self, request):
        latest_riddles = Riddle.objects.order_by("-pub_date")[:5]
        return render(request, "index.html", {"latest_riddles": latest_riddles})


class DetailView(View):
    def get(self, request, riddle_id):
        riddle = get_object_or_404(Riddle, pk=riddle_id)
        return render(request, "answer.html", {"riddle": riddle})


class AnswerView(View):
    def post(self, request, riddle_id):
        riddle = get_object_or_404(Riddle, pk=riddle_id)
        try:
            option = riddle.option_set.get(pk=request.POST["option"])
        except (KeyError, Option.DoesNotExist):
            return render(
                request,
                "answer.html",
                {"riddle": riddle, "error_message": "Option does not exist"},
            )
        else:
            if option.correct:
                latest_riddles = Riddle.objects.order_by("-pub_date")[:5]
                return render(
                    request,
                    "index.html",
                    {
                        "latest_riddles": latest_riddles,
                        "message": "Nice! Choose another one!",
                    },
                )
            else:
                return render(
                    request,
                    "answer.html",
                    {"riddle": riddle, "error_message": "Wrong Answer!"},
                )
