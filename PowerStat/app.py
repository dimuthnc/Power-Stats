
from flask import Flask, jsonify
from flask import request
from databaseaccess import insert_ecb_stats,get_ecb_stats
import uuid

app = Flask(__name__)

def persistData():
    return True



@app.route('/publish', methods=['POST'])
def publishData():
    r = request.get_json()
    residentId = r['ResidentID']
    timestamp = r['TimeStamp']
    voltage = r['Voltage']
    current = r['Current']
    phaseAnagel = r['PhaseAngel']
    status = insert_ecb_stats(str(uuid.uuid1()), residentId, timestamp, voltage, current, phaseAnagel)
    if(status):
        return jsonify(
            status="success"
        )
    else:
        return jsonify(
            status="Failed"
        )

@app.route("/data/<customer>")
def data(customer):
    assert customer == request.view_args['customer']
    get_ecb_stats('kasun')



if __name__ == '__main__':
    app.run()


