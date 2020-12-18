using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Threading.Tasks;

namespace ReadPositive.Client
{
    public class UserInfo
    {
        public List<string> UserPostSummary { get; set; } = new List<string>();

        public string UserName { get; set; } = "Anonymous";
        public string Company { get; set; } = "DC Private";

        public event Action StateHasChanged;
        public void RaiseStateHasChanged()
        {
            StateHasChanged?.Invoke();
        }

        public bool IsUserPost(string summary)
        {
            if (summary == null)
                return false;

            summary = summary.ToLower();
            return UserPostSummary.Where(p => p.ToLower().Equals(summary)).Any();
        }
    }
}
