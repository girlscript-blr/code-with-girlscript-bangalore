import 'package:flutter/material.dart';

class ProfileInfoListContainer extends StatelessWidget {
  final String title;
  final dynamic value;

  const ProfileInfoListContainer({this.title, this.value});

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20.0),
      ),
      child: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Row(
          children: [
            Expanded(
              flex: 4,
              child: Text(
                title,
                textScaleFactor: 1.3,
                style: TextStyle(
                  color: Theme.of(context).primaryColor,
                ),
              ),
            ),
            Expanded(
              child: Text(
                '$value',
                textScaleFactor: 1.3,
                style: TextStyle(
                  color: Theme.of(context).primaryColor,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
