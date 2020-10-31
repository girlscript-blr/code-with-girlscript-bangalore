import 'package:flutter/material.dart';

class CustomListContainer extends StatelessWidget {
  final int id;
  final String name;
  final String phNo;
  final String emergencyNo;
  final int age;
  final String gender;
  final String bloodType;
  final int weight;
  final int height;
  final String symptoms;
  final String date;

  const CustomListContainer(
      {Key key,
      @required this.id,
      @required this.name,
      @required this.phNo,
      @required this.emergencyNo,
      @required this.age,
      @required this.gender,
      @required this.bloodType,
      @required this.weight,
      @required this.height,
      @required this.symptoms,
      @required this.date})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20.0),
      ),
      child: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          children: [
            Text(
              name,
              textScaleFactor: 2,
              textAlign: TextAlign.center,
              style: TextStyle(
                color: Theme.of(context).primaryColor,
              ),
            ),
            const SizedBox(
              height: 10,
            ),
            buildListItems(
              context,
              title: 'ID',
              value: id,
            ),
            const SizedBox(
              height: 10,
            ),
            buildListItems(
              context,
              title: 'Phone number',
              value: phNo,
            ),
            const SizedBox(
              height: 10,
            ),
            buildListItems(
              context,
              title: 'Emergency Phone Number',
              value: emergencyNo,
            ),
            const SizedBox(
              height: 10,
            ),
            buildListItems(
              context,
              title: 'Age',
              value: age,
            ),
            const SizedBox(
              height: 10,
            ),
            buildListItems(
              context,
              title: 'Gender',
              value: gender,
            ),
            const SizedBox(
              height: 10,
            ),
            buildListItems(
              context,
              title: 'Blood Type',
              value: bloodType,
            ),
            const SizedBox(
              height: 10,
            ),
            buildListItems(
              context,
              title: 'Height',
              value: height,
            ),
            const SizedBox(
              height: 10,
            ),
            buildListItems(
              context,
              title: 'Weight',
              value: weight,
            ),
            const SizedBox(
              height: 10,
            ),
            buildListItems(
              context,
              title: 'Symptoms',
              value: symptoms,
            ),
            const SizedBox(
              height: 10,
            ),
            buildListItems(
              context,
              title: 'Date',
              value: date,
            ),
          ],
        ),
      ),
    );
  }

  Row buildListItems(BuildContext context, {String title, dynamic value}) {
    return Row(
      children: [
        Expanded(
          flex: 2,
          child: Text(
            '$title:',
            textScaleFactor: 1.5,
            style: TextStyle(
              color: Theme.of(context).primaryColor,
            ),
          ),
        ),
        Expanded(
          child: Text(
            '$value',
            textScaleFactor: 1.3,
            textAlign: TextAlign.end,
            style: TextStyle(
              color: Theme.of(context).primaryColor,
            ),
          ),
        ),
      ],
    );
  }
}
