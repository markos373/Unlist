using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

// This is the code for your desktop app.
// Press Ctrl+F5 (or go to Debug > Start Without Debugging) to run your app.

namespace UnlistGUI
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            // Click on the link below to continue learning how to build a desktop app using WinForms!
            System.Diagnostics.Process.Start("http://aka.ms/dotnet-get-started-desktop");

        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Thanks!");
        }

        private void HelloWorldLabel_Click(object sender, EventArgs e)
        {

        }

        private void Submit_Click(object sender, EventArgs e)
        {
            File.WriteAllText("credentials.txt",User.Text + ":" + Pass.Text);
            FileInfo emails = new FileInfo("emails.txt");
            if (IsFileLocked(emails)) {
            }
            int count = 0;
            using (StreamReader readtext = new StreamReader("emails.txt"))
            {
                while (!readtext.EndOfStream)
                {
                    string readMeText = readtext.ReadLine();
                    UnsubList.Items.Insert(count, readMeText);
                    count++;
                }
            }
        }
        private bool IsFileLocked(FileInfo file)
        {
            FileStream stream = null;

            try
            {
                stream = file.Open(FileMode.Open, FileAccess.ReadWrite, FileShare.None);
            }
            catch (IOException)
            {
                return true;
            }
            finally
            {
                if (stream != null)
                    stream.Close();
            }

            return false;
        }
        private void UnsubList_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void Unsubscribe_Click(object sender, EventArgs e)
        {
            string checkedItems = string.Empty;
            foreach (object Item in UnsubList.CheckedItems)
            {
                checkedItems += Item.ToString();
            }
            MessageBox.Show(checkedItems);
        }
    }
}
