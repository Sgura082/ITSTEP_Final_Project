from .models import Visitor, Tour
import time


def tour_update():
        V_data = Visitor.objects.filter()
        T_data = Tour.objects.filter()
        for Mtour in T_data:
            tour_vis_num =0
            for visitor in V_data:
                V_tours = visitor.chosen_tour
                for tour in V_tours:
                    if tour == Mtour:
                        tour_vis_num += 1
            Mtour.tour_current_visitorN = tour_vis_num
