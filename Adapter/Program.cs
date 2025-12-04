using System;
using AdapterDemo.Framework;
using AdapterDemo.Framework.Plugins;

var dashboard = new Dashboard(new Spreadsheet());
dashboard.Render(new EarthAdapter(new Earth()));