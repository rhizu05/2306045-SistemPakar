from experta import *

class Diagnosis(KnowledgeEngine):

    @Rule(Fact(cough=True) & Fact(fever=True) & Fact(fatigue=True))
    def flu(self):
        print("Diagnosis: You may have the flu.")

    @Rule(Fact(cough=True) & Fact(fever=True) & Fact(breathing_difficulty=True))
    def pneumonia(self):
        print("Diagnosis: You may have Pneumonia.")

    @Rule(Fact(sneezing=True) & Fact(runny_nose=True) & Fact(cough=False))
    def cold(self):
        print("Diagnosis: You may have a Common Cold.")

    @Rule(Fact(sore_throat=True) & Fact(fever=True))
    def throat_infection(self):
        print("Diagnosis: You may have a Throat Infection.")

    @Rule(Fact(cough=False) & Fact(fever=False) & Fact(fatigue=False))
    def healthy(self):
        print("Diagnosis: You may seem to be healthy.")

    @Rule(Fact(cough=True) & Fact(fever=True) & Fact(loss_of_taste_smell=True))
    def covid19(self):
        print("Diagnosis: You may have COVID-19.")

    @Rule(Fact(sneezing=True) & Fact(runny_nose=True) & Fact(itchy_eyes=True))
    def allergic_rhinitis(self):
        print("Diagnosis: You may have Allergic Rhinitis.")

    @Rule(Fact(wheezing=True) & Fact(breathing_difficulty=True) & Fact(cough=True))
    def asthma(self):
        print("Diagnosis: You may have Asthma.")

    @Rule(Fact(sore_throat=True) & Fact(swollen_tonsils=True) & Fact(fever=True))
    def tonsillitis(self):
        print("Diagnosis: You may have Tonsillitis.")

def get_input():
    """Helper function to get user input as boolean (yes/no)."""
    def ask_question(question):
        return input(question + " (yes/no): ").strip().lower() == "yes"

    return {
        "cough": ask_question("Do you have a cough?"),
        "fever": ask_question("Do you have a fever?"),
        "fatigue": ask_question("Do you feel fatigued?"),
        "breathing_difficulty": ask_question("Do you have breathing difficulties?"),
        "sneezing": ask_question("Are you sneezing?"),
        "runny_nose": ask_question("Do you have a runny nose?"),
        "sore_throat": ask_question("Do you have a sore throat?"),
        "loss_of_taste_smell": ask_question("Have you lost your sense of taste or smell?"),
        "itchy_eyes": ask_question("Do you have itchy eyes?"),
        "wheezing": ask_question("Are you wheezing?"),
        "swollen_tonsils": ask_question("Are your tonsils swollen?")
    }

# Running the Expert System
if __name__ == "__main__":
    symptoms = get_input()
    engine = Diagnosis()
    engine.reset()

    for symptom, present in symptoms.items():
        engine.declare(Fact(**{symptom: present}))

    engine.run()