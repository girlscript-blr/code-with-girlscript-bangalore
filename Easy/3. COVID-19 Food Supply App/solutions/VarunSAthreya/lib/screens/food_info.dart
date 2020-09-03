import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../models/user_data.dart';
import '../widgets/custom_list_container.dart';

class FoodInfo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final Map<String, int> foodInfo =
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
                      padding: const EdgeInsets.all(50.0),
                      child: Column(
                        children: [
                          CustomListContainer(
                            title: 'Rice in Kg per day',
                            value: foodInfo['rice'],
                          ),
                          const SizedBox(height: 5),
                          CustomListContainer(
                            title: 'Dal in Kg per day',
                            value: foodInfo['dal'],
                          ),
                          const SizedBox(height: 5),
                          CustomListContainer(
                            title: 'Ceralic',
                            value: foodInfo['ceralic'],
                          ),
                          const SizedBox(height: 5),
                          CustomListContainer(
                            title: 'Amul powder',
                            value: foodInfo['amul'],
                          ),
                          const SizedBox(height: 5),
                          CustomListContainer(
                            title: 'Nandini Milk TetraPacks',
                            value: foodInfo['milk'],
                          ),
                          const SizedBox(height: 5),
                          CustomListContainer(
                            title: 'Bread',
                            value: foodInfo['bread'],
                          ),
                          const SizedBox(height: 5),
                          CustomListContainer(
                            title: 'Tiger/Parle G Biscuits',
                            value: foodInfo['biscuits'],
                          ),
                          const SizedBox(height: 5),
                          CustomListContainer(
                            title: 'Canned Veggies',
                            value: foodInfo['veggis'],
                          ),
                          const SizedBox(height: 5),
                          CustomListContainer(
                            title: 'Canned Fruits',
                            value: foodInfo['fruits'],
                          ),
                          const SizedBox(height: 5),
                          CustomListContainer(
                            title: 'Medicine Packs',
                            value: foodInfo['medicine'],
                          ),
                          const SizedBox(height: 5),
                          CustomListContainer(
                            title: 'Calcium Sandoz Tablets',
                            value: foodInfo['calcTab'],
                          ),
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
