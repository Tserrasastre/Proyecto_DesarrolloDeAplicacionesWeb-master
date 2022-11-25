from src.ApiMongoDB import ApiMongoDB
import pytest

correct = {"documents":[{"_id":{"$oid":"636295da471e833ce5fdda47"},"brand":"canyon","fork":"Rock","group_sproket":"1x12","model":"Neuron 5","size":{"$numberInt":"45"},"transmission":"Shimano Deore","weight":{"$numberInt":"15"},"price_day":{"$numberInt":"50"},"price_hour":{"$numberInt":"7"},"availible":"no","location":"soller"},{"_id":{"$oid":"6362968b0043acfc00b4d816"},"brand":"orbea","fork":"Rock","group_sproket":"1x12","model":"Alma M51","size":{"$numberInt":"52"},"transmission":"SRAM Stylo","weight":{"$numberInt":"15"},"price_day":{"$numberInt":"45"},"price_hour":{"$numberInt":"7"},"availible":"no","location":"palma"},{"_id":{"$oid":"6362969c0043acfc00b4d818"},"brand":"specialized","fork":"Rock","group_sproket":"1x12","model":"Chisel","size":{"$numberInt":"60"},"transmission":"SRAM SX Eagle","weight":{"$numberInt":"14"},"price_day":{"$numberInt":"47"},"price_hour":{"$numberInt":"8"},"availible":"no","location":"palma"}]}

@pytest.mark.ApiMongoDB
def testApiMongoDB():
    assert ApiMongoDB(correct) == True