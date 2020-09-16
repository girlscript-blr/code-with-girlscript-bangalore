import 'dart:collection';
import 'package:flutter/foundation.dart';

import 'monthy_quantity_price_mixin.dart';
import 'user.dart';

class UserData extends ChangeNotifier {
  final List<User> _user = [];
  int get userCount {
    return _user.length;
  }

  UnmodifiableListView<User> get users {
    return UnmodifiableListView(_user);
  }

  void addUser({
    String aadhar,
    String name,
    String gender,
    int age,
    int rice,
    int dal,
    String specialFood1,
    String specialFood2,
  }) {
    _user.add(User(
      aadhar: aadhar,
      name: name,
      gender: gender,
      age: age,
      rice: rice,
      dal: dal,
      specialFood1: specialFood1,
      specialFood2: specialFood2,
    ));
    notifyListeners();
  }

  Map<String, int> proflieInfoCounter() {
    if (_user.isEmpty) return {};

    Map<String, int> profileInfo = {};

    int infant = 0;
    int children = 0;
    int old = 0;
    int adultM = 0;
    int adultF = 0;
    int adultO = 0;

    for (int i = 0; i < _user.length; i++) {
      if (_user[i].age < 2) {
        infant++;
      } else if (_user[i].age < 18) {
        children++;
      } else if (_user[i].age < 70) {
        switch (_user[i].gender) {
          case "Male":
            adultM++;
            break;
          case "Female":
            adultF++;
            break;
          default:
            adultO++;
        }
      } else {
        old++;
      }
    }

    profileInfo['infant'] = infant;
    profileInfo['children'] = children;
    profileInfo['old'] = old;
    profileInfo['adultM'] = adultM;
    profileInfo['adultF'] = adultF;
    profileInfo['adultO'] = adultO;

    notifyListeners();

    return profileInfo;
  }

  Map<String, List> foodInfoCounter() {
    if (_user.isEmpty) return {};

    Map<String, List> foodInfo = {};

    double rice = 0;
    double dal = 0;
    int ceralic = 0;
    int amul = 0;
    int milk = 0;
    int bread = 0;
    int biscuits = 0;
    int veggis = 0;
    int fruits = 0;
    int medicine = 0;
    int calcTab = 0;

    for (int i = 0; i < _user.length; i++) {
      rice += _user[i].rice;
      dal += _user[i].dal;

      switch (_user[i].specialFood1) {
        case 'Cerelac':
          ceralic++;
          break;
        case 'Amul powder':
          amul++;
          break;
        case 'Nandini Milk TetraPacks':
          milk++;
          break;
        case 'Bread':
          bread++;
          break;
        case 'Tiger/Parle G':
          biscuits++;
          break;
        case 'Canned Fruits':
          fruits++;
          break;
        case 'Canned Veggies':
          veggis++;
          break;
        case 'Medicine Packs':
          medicine++;
          break;
        case 'Calcium Sandoz Tablets':
          calcTab++;
          break;
        default:
          break;
      }

      switch (_user[i].specialFood2) {
        case 'Cerelac':
          ceralic++;
          break;
        case 'Amul powder':
          amul++;
          break;
        case 'Nandini Milk TetraPacks':
          milk++;
          break;
        case 'Bread':
          bread++;
          break;
        case 'Tiger/Parle G':
          biscuits++;
          break;
        case 'Canned Fruits':
          fruits++;
          break;
        case 'Canned Veggies':
          veggis++;
          break;
        case 'Medicine Packs':
          medicine++;
          break;
        case 'Calcium Sandoz Tablets':
          calcTab++;
          break;
        default:
          break;
      }
    }

    rice = rice / 1000;
    dal = dal / 1000;

    foodInfo['rice'] = [
      rice,
      MonthlyQuantity.rice,
      (rice * MonthlyQuantity.rice * MonthlyPrice.rice).round()
    ];
    foodInfo['dal'] = [
      dal,
      MonthlyQuantity.dal,
      (dal * MonthlyQuantity.dal * MonthlyPrice.dal).round()
    ];
    foodInfo['ceralic'] = [
      ceralic,
      MonthlyQuantity.ceralic,
      (ceralic * MonthlyQuantity.ceralic * MonthlyPrice.ceralic).round()
    ];
    foodInfo['amul'] = [
      amul,
      MonthlyQuantity.amul,
      (amul * MonthlyQuantity.amul * MonthlyPrice.amul).round()
    ];
    foodInfo['milk'] = [
      milk,
      MonthlyQuantity.milk,
      (milk * MonthlyQuantity.milk * MonthlyPrice.milk).round()
    ];
    foodInfo['bread'] = [
      bread,
      MonthlyQuantity.bread,
      (bread * MonthlyQuantity.bread * MonthlyPrice.bread).round()
    ];
    foodInfo['biscuits'] = [
      biscuits,
      MonthlyQuantity.biscuits,
      (biscuits * MonthlyQuantity.biscuits * MonthlyPrice.biscuits).round()
    ];
    foodInfo['veggis'] = [
      veggis,
      MonthlyQuantity.veggis,
      (veggis * MonthlyQuantity.veggis * MonthlyPrice.veggis).round()
    ];
    foodInfo['fruits'] = [
      fruits,
      MonthlyQuantity.fruits,
      (fruits * MonthlyQuantity.fruits * MonthlyPrice.fruits).round()
    ];
    foodInfo['medicine'] = [
      medicine,
      MonthlyQuantity.medicine,
      (medicine * MonthlyQuantity.medicine * MonthlyPrice.medicine).round()
    ];
    foodInfo['calcTab'] = [
      calcTab,
      MonthlyQuantity.calcTab,
      (calcTab * MonthlyQuantity.calcTab * MonthlyPrice.calcTab).round()
    ];

    foodInfo['total'] = [
      (foodInfo['rice'][2] +
              foodInfo['dal'][2] +
              foodInfo['ceralic'][2] +
              foodInfo['amul'][2] +
              foodInfo['milk'][2] +
              foodInfo['bread'][2] +
              foodInfo['biscuits'][2] +
              foodInfo['veggis'][2] +
              foodInfo['fruits'][2] +
              foodInfo['medicine'][2] +
              foodInfo['calcTab'][2])
          .round(),
    ];

    notifyListeners();

    return foodInfo;
  }
}
