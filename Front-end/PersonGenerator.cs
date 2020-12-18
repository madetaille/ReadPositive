using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ReadPositive.Client
{
    public class PersonGenerator
    {
        private Dictionary<string, string> nameToPicture = new Dictionary<string, string>();

        private Stack<string> availablePictureURL = new Stack<string>(
            new List<string>()
            {
                "../css/Picture/user9.PNG",
                "../css/Picture/user2.PNG",
                "../css/Picture/user5.PNG",
                "../css/Picture/user6.PNG",
                "../css/Picture/user7.PNG",
                "../css/Picture/user8.PNG",
            });

        public string GetPictureURL(string name)
        {
            if (nameToPicture.ContainsKey(name))
                return nameToPicture[name];

            if (availablePictureURL.Any())
                nameToPicture[name] = availablePictureURL.Pop();
            else
                return GetFallback();

            return nameToPicture[name];
        }

        private string GetFallback()
        {
            return "../css/Picture/user9.PNG";
        }
    }
}
