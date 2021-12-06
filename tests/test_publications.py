import pytest
from pages.publications import PublicationsPage
from pages.landing_page import LandingPage
from pages.add_publication import AddPublicationPage
from pages.publication_detail import PublicationDetailPage
from utils.custom_logger import LogGen
import time


class TestLandingPage:
    logger = LogGen.loggen()

    @pytest.mark.parametrize(
        "testcase_id", ["[E2E] Add Publication - happy path"]
    )
    def test_publications(self, setup, testcase_id):
        self.logger.info(
            f"******************** {testcase_id} ********************"
        )
        self.driver = setup

        # Login
        login_page = LandingPage(driver=self.driver)
        login_page.login()
        time.sleep(5)  # give some time to finish the request
        assert (
            self.driver.current_url
            == "http://localhost:3000/dashboard/publicaciones"
        )

        # Go to Add Publication page
        publications_page = PublicationsPage(driver=self.driver)
        initial_publication_count = len(publications_page.get_publications())
        publications_page.click_add_button()

        # Add a publication by filling valid values
        add_publication_page = AddPublicationPage(driver=self.driver)
        add_publication_page.fill_inputs_valid()

        # Assert that a success alert appears at the bottom
        assert add_publication_page.get_snackbar("Publicación creada.")

        # Assert that we're on detail page and the data matches
        detail_page = PublicationDetailPage(driver=self.driver)
        assert detail_page.get_title("Titulo")
        assert detail_page.get_pub_type("Mascota Perdida")
        assert detail_page.get_pet_name("Nombre")
        assert detail_page.get_pet_race("Raza")
        markers = detail_page.get_markers()
        assert len(markers) == 1

        # Delete publication
        detail_page.delete_publication()
        assert detail_page.get_snackbar("Publicación eliminada.")

        # Assert that len(publications) == initial_publication_count
        publications_count = len(publications_page.get_publications())
        assert publications_count == initial_publication_count
