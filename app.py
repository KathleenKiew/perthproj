#!/usr/bin/env python
# coding: utf-8

# In[39]:


from flask import Flask
app = Flask(__name__)


# In[40]:


from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        SUBURB_code=request.form.get("SUBURB_code")
        BEDROOMS = request.form.get("BEDROOMS")
        BATHROOMS = request.form.get("BATHROOMS")
        CBD_DIST = request.form.get("CBD_DIST")
        model = joblib.load("Perthhousing2")
        pred = model.predict([[float(SUBURB_code),float(BEDROOMS), float(BATHROOMS), float(CBD_DIST)]])
        s = "Your predicted house price will be" + str(pred)
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "Error"))


# In[ ]:


app.run()


# In[ ]:




