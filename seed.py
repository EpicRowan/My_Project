
from sqlalchemy import func

from model import Building, SoftStory, TallBuilding, connect_to_db, db

from server import app

import csv


def load_soft_story_status(soft_filename):
    """Load buildings from soft story csv into database."""

    print("Soft-Story Buildings")

    with open(soft_filename) as csvfile:
        data = csv.reader(csvfile)

        for row in data:
            address, status = row

            soft_story = SoftStory(status=status)
            building = Building(address=address)
            soft_story.building = building


            # We need to add to the session or it won't ever be stored
            db.session.add(soft_story)
            print(soft_story)

    # Once we're done, we should commit our work
    db.session.commit()

def load_tall_building(tall_filename):

    """Load buildings from tall buildings csv into database."""

    print("Tall Buildings")

    with open(tall_filename) as csvfile:
        data = csv.reader(csvfile)

    for i, row in enumerate(open(tall_filename)):
        row = row.rstrip()
        name, address, at_risk, liquefaction = row.split(",")

        at_risk = at_risk == "yes"

        tall_building = TallBuilding(name=name, at_risk = at_risk, liquefaction=liquefaction)
        building = Building(address=address)
        tall_building.building = building

        # We need to add to the session or it won't ever be stored
        db.session.add(tall_building)

    # Once we're done, we should commit our work
    db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    #csv file names and locations

    soft_filename = "seed_data/Soft-Story_Properties_clean.csv"
    tall_filename = "seed_data/Tall_Building_Inventory_clean.csv"
    
    #function calls

    load_soft_story_status(soft_filename)
    load_tall_building(tall_filename)
   