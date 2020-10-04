import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../models/user_data.dart';
import '../widgets/custom_dropdown.dart';
import '../widgets/custom_text_filed.dart';

class AddUser extends StatefulWidget {
  @override
  _AddUserState createState() => _AddUserState();
}

class _AddUserState extends State<AddUser> {
  String name;
  String phNo;
  String emergencyNo;
  int age;
  String gender = 'Gender';
  String bloodType = 'Blood Type';
  int weight;
  int height;
  String symptoms;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Theme.of(context).backgroundColor,
      body: SafeArea(
        child: SingleChildScrollView(
          child: Padding(
            padding: const EdgeInsets.all(30.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  'Enter the Details',
                  textScaleFactor: 2,
                  style: TextStyle(
                    color: Theme.of(context).primaryColor,
                    fontFamily: 'Popins',
                  ),
                ),
                const SizedBox(
                  height: 30.0,
                ),
                CustomTextField(
                  title: 'Enter Your Name',
                  labelText: 'Name',
                  textCapitalization: TextCapitalization.sentences,
                  onChanged: (newText) {
                    setState(() {
                      name = newText.toString();
                    });
                  },
                ),
                const SizedBox(
                  height: 20,
                ),
                CustomTextField(
                  title: 'Enter Your Phone Number',
                  labelText: 'Phone Number',
                  textCapitalization: TextCapitalization.sentences,
                  keyboardType: TextInputType.number,
                  onChanged: (newText) {
                    setState(() {
                      phNo = newText.toString();
                    });
                  },
                ),
                const SizedBox(
                  height: 20,
                ),
                CustomTextField(
                  title: 'Enter Emergency Phone Number',
                  labelText: 'Emergency Phone Number',
                  textCapitalization: TextCapitalization.sentences,
                  keyboardType: TextInputType.number,
                  onChanged: (newText) {
                    setState(() {
                      emergencyNo = newText.toString();
                    });
                  },
                ),
                const SizedBox(
                  height: 20,
                ),
                CustomTextField(
                  title: 'Enter Your Age',
                  labelText: 'Age',
                  textCapitalization: TextCapitalization.sentences,
                  keyboardType: TextInputType.number,
                  onChanged: (newText) {
                    setState(() {
                      age = int.parse(newText.toString());
                    });
                  },
                ),
                const SizedBox(
                  height: 20,
                ),
                CustomDropDown(
                  list: const ['Male', 'Female', 'Other'],
                  title: "Select your Gender",
                  value: gender,
                  onChanged: (val) {
                    FocusScope.of(context).requestFocus(FocusNode());
                    setState(() {
                      gender = val.toString();
                    });
                  },
                ),
                const SizedBox(
                  height: 20,
                ),
                CustomTextField(
                  title: 'Enter your Height in cm',
                  labelText: 'Height',
                  textCapitalization: TextCapitalization.sentences,
                  keyboardType: TextInputType.number,
                  onChanged: (newText) {
                    setState(() {
                      height = int.parse(newText.toString());
                    });
                  },
                ),
                const SizedBox(
                  height: 20,
                ),
                CustomTextField(
                  title: 'Enter your Weight in Kg',
                  labelText: 'Weight',
                  textCapitalization: TextCapitalization.sentences,
                  keyboardType: TextInputType.number,
                  onChanged: (newText) {
                    setState(() {
                      weight = int.parse(newText.toString());
                    });
                  },
                ),
                const SizedBox(
                  height: 20,
                ),
                CustomDropDown(
                  list: const [
                    'A+',
                    'A-',
                    'B+',
                    'B-',
                    'AB+',
                    'AB-',
                    'O+',
                    'O-',
                  ],
                  title: "Select your Blood type",
                  value: bloodType,
                  onChanged: (val) {
                    FocusScope.of(context).requestFocus(FocusNode());
                    setState(() {
                      bloodType = val.toString();
                    });
                  },
                ),
                const SizedBox(
                  height: 20,
                ),
                CustomTextField(
                  title: 'Enter Your Symptom',
                  labelText: 'Symptom',
                  textCapitalization: TextCapitalization.sentences,
                  onChanged: (newText) {
                    setState(() {
                      symptoms = newText.toString();
                    });
                  },
                ),
              ],
            ),
          ),
        ),
      ),
      bottomNavigationBar: buildBottomBar(context),
    );
  }

  Padding buildBottomBar(BuildContext context) {
    bool shouldSubmit = name != null &&
        phNo != null &&
        emergencyNo != null &&
        age != null &&
        gender != 'Gender' &&
        bloodType != 'Blood Type' &&
        weight != null &&
        height != null &&
        symptoms != null;

    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Container(
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(10.0),
          gradient: LinearGradient(
            colors: shouldSubmit
                ? [
                    Theme.of(context).primaryColor,
                    Theme.of(context).accentColor,
                  ]
                : [
                    Colors.grey[700],
                    Colors.grey,
                  ],
          ),
        ),
        child: FlatButton(
          onPressed: () {
            if (shouldSubmit) {
              Provider.of<UserData>(context, listen: false).addUser(
                name: name,
                phNo: phNo,
                emergencyNo: emergencyNo,
                age: age,
                gender: gender,
                bloodType: bloodType,
                weight: weight,
                height: height,
                symptoms: symptoms,
              );
              Navigator.pop(context);
            } else {
              return null;
            }
          },
          child: const Text(
            'Submit',
            textScaleFactor: 1.5,
            style: TextStyle(color: Colors.white),
          ),
        ),
      ),
    );
  }
}
