import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../models/user_data.dart';
import '../widgets/food_info_list_container.dart';
import '../widgets/profile_info_list_container.dart';

class FoodInfo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final Map<String, List> foodInfo =
        Provider.of<UserData>(context, listen: false).foodInfoCounter();
    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [
              Theme.of(context).primaryColor,
              Theme.of(context).accentColor,
            ],
          ),
        ),
        alignment: Alignment.center,
        child: SafeArea(
          child: SingleChildScrollView(
            child: Padding(
              padding: const EdgeInsets.all(20.0),
              child: Column(
                children: [
                  const Text(
                    'Food Info',
                    textScaleFactor: 3.0,
                    style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                      fontFamily: 'Popins',
                      letterSpacing: 2.0,
                    ),
                  ),
                  const SizedBox(
                    height: 30,
                  ),
                  Container(
                    decoration: BoxDecoration(
                      color: Theme.of(context).backgroundColor,
                      borderRadius: BorderRadius.circular(30.0),
                    ),
                    child: Padding(
                      padding: const EdgeInsets.all(30.0),
                      child: foodInfo.isEmpty
                          ? Container(
                              decoration: BoxDecoration(
                                color: Colors.white,
                                borderRadius: BorderRadius.circular(20.0),
                              ),
                              child: Text(
                                'No Users Added',
                                textScaleFactor: 1.5,
                                style: TextStyle(
                                  color: Theme.of(context).primaryColor,
                                ),
                              ),
                            )
                          : Column(
                              children: [
                                FoodInfoListContainer(
                                  title: 'Rice in Kg per day',
                                  values: foodInfo['rice'],
                                ),
                                const SizedBox(height: 15),
                                FoodInfoListContainer(
                                  title: 'Dal in Kg per day',
                                  values: foodInfo['dal'],
                                ),
                                const SizedBox(height: 15),
                                FoodInfoListContainer(
                                  title: 'Cerelac 1 pack',
                                  values: foodInfo['ceralic'],
                                ),
                                const SizedBox(height: 15),
                                FoodInfoListContainer(
                                  title: 'Amul powder 1Kg',
                                  values: foodInfo['amul'],
                                ),
                                const SizedBox(height: 15),
                                FoodInfoListContainer(
                                  title: 'Nandini Milk TetraPacks 1lt',
                                  values: foodInfo['milk'],
                                ),
                                const SizedBox(height: 15),
                                FoodInfoListContainer(
                                  title: 'Bread loaf 1pack',
                                  values: foodInfo['bread'],
                                ),
                                const SizedBox(height: 15),
                                FoodInfoListContainer(
                                  title: 'Tiger/Parle G Biscuits 5pieces Pack	',
                                  values: foodInfo['biscuits'],
                                ),
                                const SizedBox(height: 15),
                                FoodInfoListContainer(
                                  title: 'Canned Veggies',
                                  values: foodInfo['veggis'],
                                ),
                                const SizedBox(height: 15),
                                FoodInfoListContainer(
                                  title: 'Canned Fruits',
                                  values: foodInfo['fruits'],
                                ),
                                const SizedBox(height: 15),
                                FoodInfoListContainer(
                                  title: 'Medicine Packs',
                                  values: foodInfo['medicine'],
                                ),
                                const SizedBox(height: 15),
                                FoodInfoListContainer(
                                  title: 'Calcium Sandoz Tablets',
                                  values: foodInfo['calcTab'],
                                ),
                                const SizedBox(height: 15),
                                ProfileInfoListContainer(
                                  title: 'Total',
                                  value: foodInfo['total'][0],
                                )
                              ],
                            ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
