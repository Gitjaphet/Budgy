from django.db import models

class Depense(models.Model):
    CATEGORIES = [
        ('alimentation', 'Alimentation'),
        ('transport', 'Transport'),
        ('logement', 'Logement'),
        ('sante', 'Santé'),
        ('loisirs', 'Loisirs'),
        ('autre', 'Autre'),
    ]

    titre = models.CharField(max_length=200)
    montant = models.DecimalField(max_digits=10, decimal_places=0)
    categorie = models.CharField(max_length=50, choices=CATEGORIES, default='autre')
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titre} : {self.montant} Ar"

    class Meta:
        db_table = "depense"
        ordering = ['-date']