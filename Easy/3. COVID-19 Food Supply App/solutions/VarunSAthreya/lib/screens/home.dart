import 'package:flutter/material.dart';

import 'add_user.dart';
import 'food_info.dart';
import 'person_info.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
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
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                const Text(
                  'Select One',
                  textScaleFactor: 4.0,
                  style: TextStyle(
                    color: Colors.white,
                    fontFamily: 'Popins',
                  ),
                ),
                Container(
                  decoration: BoxDecoration(
                    color: Theme.of(context).backgroundColor,
                    borderRadius: BorderRadius.circular(30.0),
                  ),
                  child: Padding(
                    padding: const EdgeInsets.all(50.0),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        buildNavigoationButton(
                          context: context,
                          title: 'Add user',
                          onPressed: () => Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) => AddUser(),
                              )),
                        ),
                        const SizedBox(
                          height: 20,
                        ),
                        buildNavigoationButton(
                          context: context,
                          title: 'Person Info',
                          onPressed: () => Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) => PersonInfo(),
                              )),
                        ),
                        const SizedBox(
                          height: 20,
                        ),
                        buildNavigoationButton(
                          context: context,
                          title: 'Food Info',
                          onPressed: () => Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) => FoodInfo(),
                              )),
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
    );
  }

  Widget buildNavigoationButton(
      {BuildContext context, String title, Function onPressed}) {
    return FlatButton(
      onPressed: () => onPressed(),
      color: Colors.white,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(30.0),
        side: BorderSide(color: Theme.of(context).primaryColor),
      ),
      child: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Text(
          title,
          textScaleFactor: 2.0,
          style: TextStyle(
            color: Theme.of(context).primaryColor,
          ),
        ),
      ),
    );
  }
}
