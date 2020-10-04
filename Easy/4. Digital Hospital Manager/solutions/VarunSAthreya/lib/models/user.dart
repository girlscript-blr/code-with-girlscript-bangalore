import 'package:flutter/foundation.dart';

class User {
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

  User({
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
    @required this.date,
  });
}
