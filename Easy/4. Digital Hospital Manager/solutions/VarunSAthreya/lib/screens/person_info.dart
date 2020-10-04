import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../models/user_data.dart';
import '../widgets/custom_list_container.dart';

class PersonInfo extends StatelessWidget {
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
            padding: const EdgeInsets.all(30.0),
            child: Consumer<UserData>(
              builder: (context, userData, child) {
                return ListView.builder(
                  itemBuilder: (context, index) {
                    final user = userData.users[index];
                    return Column(
                      children: [
                        CustomListContainer(
                          id: user.id,
                          name: user.name,
                          age: user.age,
                          gender: user.gender,
                          bloodType: user.bloodType,
                          phNo: user.phNo,
                          emergencyNo: user.emergencyNo,
                          height: user.height,
                          weight: user.weight,
                          symptoms: user.symptoms,
                          date: user.date,
                        ),
                        SizedBox(
                          height: 20,
                        ),
                      ],
                    );
                  },
                  itemCount: userData.userCount,
                );
              },
            ),
          ),
        ),
      ),
    );
  }
}
