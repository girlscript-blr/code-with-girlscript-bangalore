import 'package:flutter/material.dart';

class CustomDropDown extends StatelessWidget {
  const CustomDropDown({
    @required this.title,
    @required this.list,
    @required this.value,
    @required this.onChanged = null,
  });

  final Function onChanged;
  final String title;
  final String value;
  final List<String> list;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
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
              style: TextStyle(
                color: Theme.of(context).primaryColor.withOpacity(0.7),
              ),
            ),
            const SizedBox(
              height: 10,
            ),
            DropdownButton<String>(
              hint: Text(value),
              items: list.map((String value) {
                return DropdownMenuItem<String>(
                  value: value,
                  child: Text(value),
                );
              }).toList(),
              onChanged: (val) => onChanged(val),
            )
          ],
        ),
      ),
    );
  }
}
