from django.shortcuts import render
from .forms import CppCodeForm
from .utils import run_cpp_code


def home(request):
    context = {}
    if request.method == "POST":
        form = CppCodeForm(request.POST)
        if form.is_valid():
            cpp_code = form.cleaned_data["cppCode"]
            try:
                output, error = run_cpp_code(cpp_code)
                context = {
                    "form": form,
                    "output": output,
                    "error": error,
                }
            except Exception as e:
                context = {
                    "form": form,
                    "output": None,
                    "error": str(e),
                }
    else:
        form = CppCodeForm(initial={"cppCode": request.POST.get("cppCode", "")})
        context = {"form": form}
    return render(request, "home.html", context)
