from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Character, Equipement


def home(request):
    characters = Character.objects.all()
    equipments = Equipement.objects.all()
    return render(
        request,
        "playground/home.html",
        {"characters": characters, "equipments": equipments},
    )


def character_detail(request, id_character):
    """ancien_lieu.disponibilite = "libre"
    ancien_lieu.save()
    nouveau_lieu.disponibilite = "occupé"
    nouveau_lieu.save()"""
    character = get_object_or_404(Character, id_character=id_character)
    ancien_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
    if request.method == "POST":
        form = MoveForm(request.POST, instance=character)
        if form.is_valid():
            form.save(commit=False)
            nouveau_lieu = get_object_or_404(
                Equipement, id_equip=character.lieu.id_equip
            )
            if nouveau_lieu.disponibilite != "libre":
                character = get_object_or_404(Character, id_character=id_character)
                return render(
                    request,
                    "playground/character_detail.html",
                    {
                        "character": character,
                        "form": form,
                        "message": f"Ce lieu est occupé",
                    },
                )
            elif character.etat != nouveau_lieu.etat_prerequis:
                character = get_object_or_404(Character, id_character=id_character)
                return render(
                    request,
                    "playground/character_detail.html",
                    {
                        "character": character,
                        "form": form,
                        "message": f"le Pokémon n'est pas dans le bon état (état requis: {nouveau_lieu.etat_prerequis})",
                    },
                )
            else:
                ancien_lieu.disponibilite = "libre"
                print(ancien_lieu.id_equip)
                ancien_lieu.save()
                if nouveau_lieu.id_equip != "Boite du PC":
                    nouveau_lieu.disponibilite = "occupé"
                    nouveau_lieu.save()
                character.etat = nouveau_lieu.etat_suivant
                character.save()
            return redirect("character_detail", id_character=id_character)
    else:
        form = MoveForm()
        return render(
            request,
            "playground/character_detail.html",
            {"character": character, "form": form, "message": ""},
        )
