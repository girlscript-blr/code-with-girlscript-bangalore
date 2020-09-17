import 'package:flutter/material.dart';

class FoodInfoListContainer extends StatelessWidget {
  final String title;
  final List values;

  const FoodInfoListContainer({this.title, this.values});

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20.0),
      ),
      child: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          children: [
            Text(
              title,
              textScaleFactor: 1.5,
              textAlign: TextAlign.center,
              style: TextStyle(
                color: Theme.of(context).primaryColor,
              ),
            ),
            const SizedBox(
              height: 10,
            ),
            buildListItems(
              context,
              title: 'Required Quantity',
              value: values[0],
            ),
            const SizedBox(
              height: 10,
            ),
            buildListItems(
              context,
              title: 'Monthly Quantity',
              value: values[1],
            ),
            const SizedBox(
              height: 10,
            ),
            buildListItems(
              context,
              title: 'Price (Rs.)',
              value: values[2],
            ),
          ],
        ),
      ),
    );
  }

  Row buildListItems(BuildContext context, {String title, dynamic value}) {
    return Row(
      children: [
        Expanded(
          flex: 2,
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
            textAlign: TextAlign.end,
            style: TextStyle(
              color: Theme.of(context).primaryColor,
            ),
          ),
        ),
      ],
    );
  }
}
