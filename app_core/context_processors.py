from .models import Subject


def navbar_contexts(request):
    ial_subjects = []
    igcse_subjects = []
    all_subjects = Subject.objects.all()
    for subjects in all_subjects:
        if subjects.cat_choices == 'IAL':
            ial_subjects.append(subjects)
        else:
            igcse_subjects.append(subjects)

    context = {'IGCSE': igcse_subjects, 'IAL': ial_subjects}
    return context
