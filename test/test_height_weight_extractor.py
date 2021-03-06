import unittest

from digExtractor.extractor_processor import ExtractorProcessor
from digHeightWeightExtractor.height_weight_extractor\
    import HeightWeightExtractor


class TestHeightWeightExtractorMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_height_weight_extractor(self):
        doc = {'content': "\n TS RUBI: THE NAME SAYS IT ALL!  \n INCALL $250 OUTCALL $350 \n \n \n \n \n \n Gender \n Age \n Ethnicity \n Hair Color \n Eye Color \n Height \n Weight \n Measurements \n Affiliation \n Availability \n Available To \n \n \n \n \n Transsexual \n 27 \n Latino/Hispanic \n Brown \n Hazel \n 5'5\" \n 130 lb \n 34C - 28\" - 34\" \n ", 'b': 'world'}

        extractor = HeightWeightExtractor().set_metadata(
            {'extractor': 'height_weight'})
        ep = ExtractorProcessor().set_input_fields(['content'])\
                                 .set_output_field('extracted')\
                                 .set_extractor(extractor)
        updated_doc = ep.extract(doc)

        self.assertEqual(updated_doc['extracted'][0]['result']['value'],
                         {'weight': {'raw': [{'pound': 130}],
                                     'pound': [130],
                                     'kilogram': [58]},
                          'height': {'foot': ['5\'5"'],
                                     'raw': [{'foot': 5, 'inch': 5}],
                                     'centimeter': [165]}})

    def test_height_weight_extractor_separated(self):
        doc = {'content': "\n TS RUBI: THE NAME SAYS IT ALL!  \n INCALL $250 OUTCALL $350 \n \n \n \n \n \n Gender \n Age \n Ethnicity \n Hair Color \n Eye Color \n Height \n Weight \n Measurements \n Affiliation \n Availability \n Available To \n \n \n \n \n Transsexual \n 27 \n Latino/Hispanic \n Brown \n Hazel \n 5'5\" \n 130 lb \n 34C - 28\" - 34\" \n ", 'b': 'world'}

        extractor = HeightWeightExtractor().set_metadata(
            {'extractor': 'height_weight'})
        ep = ExtractorProcessor().set_input_fields(['content'])\
                                 .set_output_fields(['height', 'weight'])\
                                 .set_extractor(extractor)
        updated_doc = ep.extract(doc)

        self.assertEqual(updated_doc['height'][0]['result']['value'],
                         {'foot': ['5\'5"'],
                          'raw': [{'foot': 5, 'inch': 5}],
                          'centimeter': [165]})
        self.assertEqual(updated_doc['weight'][0]['result']['value'],
                         {'raw': [{'pound': 130}],
                          'pound': [130],
                          'kilogram': [58]})

    def test_height_weight_extractor_empty(self):
        doc = {'content': "\n TS RUBI: THE NAME SAYS IT ALL!  \n INCALL $250 OUTCALL $350 \n \n \n \n \n \n Gender \n Age \n Ethnicity \n Hair Color \n Eye Color \n Height \n Weight \n Measurements \n Affiliation \n Availability \n Available To \n \n \n \n \n Transsexual \n 27 \n Latino/Hispanic \n Brown \n Hazel \n 34C - 28\" - 34\" \n ", 'b': 'world'}

        extractor = HeightWeightExtractor().set_metadata(
            {'extractor': 'height_weight'})
        extractor_processor = ExtractorProcessor().set_input_fields(
            ['content']).set_output_field('extracted').set_extractor(extractor)
        updated_doc = extractor_processor.extract(doc)

        self.assertNotIn("extracted", updated_doc)


if __name__ == '__main__':
    unittest.main()
