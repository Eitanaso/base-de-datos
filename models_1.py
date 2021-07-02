from django.db import models


class Mes(models.Model):
    nombre = models.CharField(primary_key=True, max_length=255)
    numero = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mes'

        
class Game(models.Model):
    game_id = models.IntegerField(primary_key=True, blank=True, null=True)

    season_id = models.IntegerField(blank=True, null=True)

    team_id_home = models.IntegerField(blank=True, null=True)
    team_name_home = models.CharField(max_length=45)
    models.CharField(max_length=250),
    wl_home=models.CharField(max_length=250)
    fgm_home = models.FloatField()
    fga_home=models.FloatField()
    oreb_home=models.FloatField()
    dreb_home=models.FloatField()
    reb_home=models.FloatField()
    ast_home=models.FloatField()
    stl_home=models.FloatField()
    blk_home=models.FloatField()
    tov_home=models.FloatField()
    pf_home=models.FloatField()
    team_id_away=models.IntegerField(blank=True, null=True)
    team_name_away=models.CharField(max_length=50)
    wl_away=models.CharField(max_length=50)
    fgm_away=models.FloatField()
    fga_away=models.FloatField()
    oreb_away=models.FloatField()
    dreb_away=models.FloatField()
    reb_away=models.FloatField()
    ast_away=models.FloatField()
    stl_away=models.FloatField()
    blk_away=models.FloatField()
    tov_away=models.FloatField()
    pf_away=models.FloatField()
    year=models.IntegerField(blank=True, null=True)
    game_date=models.DateField()

    class Meta:
        managed = False
        db_table = 'game'