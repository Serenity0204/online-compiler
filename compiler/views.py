from django.shortcuts import render
from .forms import CppForm
from .utils import run_cpp
from django.http import HttpResponse


DEFAULT_CODE = """#include <iostream>
using namespace std;
int main() {
   cout << "Hello, World!" << endl; // This prints Hello, World!
   return 0;
}"""


def home_view(request):
    context = {}
    if request.method == "POST":
        form = CppForm(request.POST)
        if form.is_valid():
            cpp_code = form.cleaned_data["cpp"]
            try:
                output, error = run_cpp(cpp_code)
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
        form = CppForm(initial={"cpp": DEFAULT_CODE})
        context = {"form": form}
    return render(request, "home.html", context)


def download_view(request):
    code = request.GET.get("cpp", "")
    response = HttpResponse(content_type="text/x-c++src")
    response["Content-Disposition"] = 'attachment; filename="main.cpp"'
    response.write(code)
    return response
