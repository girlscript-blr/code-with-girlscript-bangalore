import 'package:flutter/foundation.dart';

class User {
  final String aadhar;
  final String name;
  final String gender;
  final int age;
  final int rice;
  final int dal;
  final String specialFood1;
  final String specialFood2;

  User({
    @required this.aadhar,
    @required this.name,
    @required this.gender,
    @required this.age,
    @required this.rice,
    @required this.dal,
    @required this.specialFood1,
    @required this.specialFood2,
  });
}
