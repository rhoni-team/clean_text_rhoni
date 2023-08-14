""" Test for main clean_text_rhoni module """

from clean_text_rhoni.clean_text_rhoni import complete_clean_text, normalize_text


raw_text = "         El azar me llevó hacia ellos una mañana de primavera en que París abrió \
su cola de pavorreal después          de la lenta invernada.!!!!!!!!! Bajé por el bulevar de \
Port-Royal, tomé St. Marcel y L'Hospital, vi los verdes entre tanto gris y me \
acordé de los leones. Era amigo de los leones y las panteras, pero nunca había \
entrado en el húmedo y oscuro edificio de los $$$acuarios. Dejé mi bicicleta \
contra las re&7jas y me     fui a ver los tulipanes. Los leones estaban feos y tristes y \
mi pantera dormía. Opté por los acuarios, soslayé peces vulgares hasta dar \
inesperadamente con los axólotl.      Me quedé una hora 1 mirándolos y salí, \
incapaz de otra cosa."


def test_complete_clean_text():
    """
    Unit test for complete_clean_text
    """
    cleaned_text = "el azar me llevo hacia ellos una manana de primavera en que paris abrio \
        su cola de pavorreal despues de la lenta invernada baje por el bulevar de \
        portroyal tome st marcel y lhospital vi los verdes entre tanto gris y me \
        acorde de los leones era amigo de los leones y las panteras pero nunca habia \
        entrado en el humedo y oscuro edificio de los acuarios deje mi bicicleta \
        contra las re7jas y me fui a ver los tulipanes los leones estaban feos y tristes y \
        mi pantera dormia opte por los acuarios soslaye peces vulgares hasta dar \
        inesperadamente con los axolotl me quede una hora 1 mirandolos y sali \
        incapaz de otra cosa"
    
    expected_text = cleaned_text.replace("        ", "")
    
    result_text = complete_clean_text(text=raw_text)

    assert expected_text == result_text
