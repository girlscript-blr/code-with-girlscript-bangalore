import 'package:flutter/material.dart';

class CustomTextField extends StatelessWidget {
  const CustomTextField({
    @required this.labelText,
    @required this.title,
    this.autofocus = false,
    this.textCapitalization = TextCapitalization.none,
    this.onChanged = null,
    this.keyboardType = TextInputType.name,
  });

  final String labelText;
  final bool autofocus;
  final TextCapitalization textCapitalization;
  final Function onChanged;
  final String title;
  final TextInputType keyboardType;

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
          crossAxisAlignment: CrossAxisAlignment.start,
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
            TextFormField(
              keyboardType: keyboardType,
              decoration: InputDecoration(
                labelText: labelText,
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(8.0),
                ),
              ),
              autofocus: autofocus,
              autocorrect: true,
              textCapitalization: textCapitalization,
              onChanged: (String str) => onChanged(str),
              cursorColor: Theme.of(context).primaryColor,
            ),
          ],
        ),
      ),
    );
  }
}
