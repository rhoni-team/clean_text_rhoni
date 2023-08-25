"""Unit tests for clean text class
"""

from clean_text_rhoni.base_clean_text import BaseCleanText


class TestBaseCleanText:
    """Class to with unit tests for CleanText
    """

    def setup_class(cls):
        """Setup tests
        """
        cls.clean_text_instance = BaseCleanText()

    def test_remove_leading_trailing_spaces(self):
        """Test BaseCleanText.remove_leading_trailing_spaces function
        """
        raw_text = "  Hubo un tiempo en que yo    pensaba mucho en los axólotl.   "
        expected_text = "Hubo un tiempo en que yo    pensaba mucho en los axólotl."
        result_text = self.clean_text_instance.remove_leading_trailing_spaces(raw_text)

        assert expected_text == result_text

    def test_transform_to_lowercase(self):
        """Test BaseCleanText.transform_to_lowercase function
        """
        raw_text = "  Hubo un Tiempo en que yo    Pensaba mucho en los axólotl.   "
        expected_text = "  hubo un tiempo en que yo    pensaba mucho en los axólotl.   "
        result_text = self.clean_text_instance.transform_to_lowercase(raw_text)

        assert expected_text == result_text

    def test_remove_accents(self):
        """Test BaseCleanText.remove_accents function
        """
        raw_text = "  Húbó un tíémpo en qué yo    pensábá mucho en los axólotl.   "
        expected_text = "  Hubo un tiempo en que yo    pensaba mucho en los axolotl.   "
        result_text = self.clean_text_instance.remove_accents(raw_text)

        assert expected_text == result_text

    def test_replace_spaces_by_underscores(self):
        """Test BaseCleanText.replace_spaces_by_underscores function
        """
        raw_text = "  Hubo un Tiempo en que yo    Pensaba mucho en los axólotl.   "
        expected_text = "__Hubo_un_Tiempo_en_que_yo____Pensaba_mucho_en_los_axólotl.___"
        result_text = self.clean_text_instance.replace_spaces_by_underscores(
            raw_text)

        assert expected_text == result_text

    def test_replace_underscores_by_spaces(self):
        """Test BaseCleanText.replace_underscores_by_spaces function
        """
        raw_text = "__Hubo_un_Tiempo_en_que_yo____Pensaba_mucho_en_los_axólotl.___"
        expected_text = "  Hubo un Tiempo en que yo    Pensaba mucho en los axólotl.   "
        result_text = self.clean_text_instance.replace_underscores_by_spaces(
            raw_text)

        assert expected_text == result_text

    def test_replace_multiple_spaces(self):
        """Test BaseCleanText.replace_multiple_spaces function
        """
        raw_text = "  Hubo un Tiempo en que yo    Pensaba mucho en los axólotl.   "
        expected_text = " Hubo un Tiempo en que yo Pensaba mucho en los axólotl. "
        result_text = self.clean_text_instance.replace_multiple_spaces(
            raw_text)

        assert expected_text == result_text
    
    def test_remove_special_characters(self):
        """Test BaseCleanText.remove_special_characters function
        """
        raw_text = "  Hubo un ##$Tiempo en!! ?que yo    Pensa-ba mu--cho en los axólot%&!l.!   "
        expected_text = "  Hubo un Tiempo en que yo    Pensaba mucho en los axólotl   "
        result_text = self.clean_text_instance.remove_special_characters(
            raw_text)
        
        assert expected_text == result_text

    def test_remove_n_tilde(self):
        """Test BaseCleanText.remove_n_tilde function
        """
        raw_text = "mañana, ñandú, ñacurutú"
        expected_text = "manana, nandú, nacurutú"
        result_text = self.clean_text_instance.remove_n_tilde(raw_text)

        assert expected_text == result_text
