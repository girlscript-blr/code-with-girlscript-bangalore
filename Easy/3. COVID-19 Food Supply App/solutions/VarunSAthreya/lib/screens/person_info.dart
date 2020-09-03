import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../models/user_data.dart';
import '../widgets/custom_list_container.dart';

class PersonInfo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final Map<String, int> profileInfo =
        Provider.of<UserData>(context, listen: false).proflieInfoCounter();
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
          child: Padding(
            padding: const EdgeInsets.all(20.0),
            child: Column(
              children: [
                const Text(
                  'Profile Info',
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
                            title: 'Infant', value: profileInfo['infant']),
                        const SizedBox(height: 5),
                        CustomListContainer(
                            title: 'Children', value: profileInfo['children']),
                        const SizedBox(height: 5),
                        CustomListContainer(
                            title: 'Adult Male', value: profileInfo['adultM']),
                        const SizedBox(height: 5),
                        CustomListContainer(
                            title: 'Adult Female',
                            value: profileInfo['adultF']),
                        const SizedBox(height: 5),
                        CustomListContainer(
                            title: 'Adult Other', value: profileInfo['adultO']),
                        const SizedBox(height: 5),
                        CustomListContainer(
                            title: 'Old', value: profileInfo['old']),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
