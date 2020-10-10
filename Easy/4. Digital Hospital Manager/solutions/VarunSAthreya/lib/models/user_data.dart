import 'dart:collection';
import 'dart:math';
import 'package:flutter/foundation.dart';

import 'user.dart';

class UserData extends ChangeNotifier {
  Random random = new Random();
  final List<User> _user = [];
  int get userCount {
    return _user.length;
  }

  UnmodifiableListView<User> get users {
    return UnmodifiableListView(_user);
  }

  void addUser({
    String name,
    String phNo,
    String emergencyNo,
    int age,
    String gender,
    String bloodType,
    int weight,
    int height,
    String symptoms,
  }) {
    _user.add(User(
      id: random.nextInt(10000),
      name: name,
      phNo: phNo,
      emergencyNo: emergencyNo,
      age: age,
      gender: gender,
      bloodType: bloodType,
      weight: weight,
      height: height,
      symptoms: symptoms,
      date: DateTime.now().toString().split(' ').first,
    ));
    notifyListeners();
  }

  void deleteTask(User user) {
    _user.remove(user);
    notifyListeners();
  }
}
