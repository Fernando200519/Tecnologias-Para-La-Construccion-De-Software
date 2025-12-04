using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AdapterDemo.Plugins;

namespace AdapterDemo.Framework
{
    public class EarthAdapter : IGraphic
    {
        private EarthAdapter earth;

        public EarthAdapter(Earth earth)
        {
            this.earth = earth;
        }

        public void Generate(Spreadsheet doc)
        {
            earth.Render(doc);
        }
    }
}