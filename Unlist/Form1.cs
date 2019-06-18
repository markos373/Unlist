using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Unlist
{
    public partial class Form1 : Form
    {
        public object Items { get; private set; }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Label1_Click(object sender, EventArgs e)
        {

        }

        private void TextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void TextBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void Button1_Click(object sender, EventArgs e)
        {
            string user = userName.Text;
            string pass = password.Text;
            System.IO.File.WriteAllText(@"D:\cs\Unlist\Unlist\src\credentials\credentials.txt", user+":"+pass);
            
            var lines = File.ReadAllLines(@"D:\cs\Unlist\Unlist\src\unsubscribeCompany.txt");
            for (var i = 0; i < lines.Length; i += 1)
            {
                var line = lines[i];
                var parts = line.Split(':');
                this.UnsubList.Items.Add(parts[0]);
                // Process line
            }
            Console.Write("test");
                
        }
        private void run_cmd(string cmd, string args)
        {
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = "my/full/path/to/python.exe";
            start.Arguments = string.Format("{0} {1}", cmd, args);
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    Console.Write(result);
                }
            }
        }

        private void Company1_SelectedIndexChanged(object sender, EventArgs e)
        {
    
        }

        private void Unsubscribe_Click(object sender, EventArgs e)
        {

        }
    }
}
