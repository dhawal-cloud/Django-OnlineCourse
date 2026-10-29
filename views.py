from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Course, Question, Choice, Submission


@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method != "POST":
        return redirect("onlinecourse:course_detail", course_id=course.id)

    questions = Question.objects.filter(course=course).prefetch_related("choices")
    score = 0
    total = questions.count()

    for question in questions:
        selected_id = request.POST.get(f"question_{question.id}")
        selected = None
        if selected_id:
            selected = Choice.objects.filter(
                pk=selected_id, question=question
            ).first()

        Submission.objects.create(
            user=request.user,
            question=question,
            selected_choice=selected,
        )
        if selected and selected.is_correct:
            score += 1

    request.session["exam_result"] = {
        "course_id": course.id,
        "course_name": course.name,
        "score": score,
        "total": total,
    }
    return redirect("onlinecourse:show_exam_result")


@login_required
def show_exam_result(request):
    result = request.session.get("exam_result")
    if not result:
        return redirect("onlinecourse:course_list")
    return render(request, "onlinecourse/exam_result.html", {"result": result})
