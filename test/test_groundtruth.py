# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-11-08 14:50:34
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-11-08 18:16:51
import sys
import time
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

import groundtruth
from digExtractor.extractor import Extractor
from digExtractor.extractor_processor import ExtractorProcessor
from digHeightWeightExtractor.height_weight_extractor import HeightWeightExtractor

class TestGroundtruthMethods(unittest.TestCase):

    def setUp(self):
        self.groundtruth_data = groundtruth.load_groundtruth()

    def tearDown(self):
        pass

    def test_height_weight_extractor(self):
        extractor = HeightWeightExtractor().set_metadata({'extractor': 'height_weight'})
        extractor_processor = ExtractorProcessor().set_input_fields(['content']).set_output_field('extracted').set_extractor(extractor)

        for doc in self.groundtruth_data[:20]:
            updated_doc = extractor_processor.extract(doc)
            self.assertIn('extracted', updated_doc)
            self.assertTrue(len(updated_doc['extracted']) > 0)
            extraction = updated_doc['extracted'][0]['value']
            # print extraction['height']
            # print extraction['weight']
            self.assertEqual(extraction['height'], doc['height'])
            self.assertEqual(extraction['weight'], doc['weight'])


    

if __name__ == '__main__':
    unittest.main()



