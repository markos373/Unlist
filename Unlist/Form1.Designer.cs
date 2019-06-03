namespace Unlist
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.userName = new System.Windows.Forms.TextBox();
            this.password = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.Submit = new System.Windows.Forms.Button();
            this.Company1 = new System.Windows.Forms.CheckedListBox();
            this.SuspendLayout();
            // 
            // userName
            // 
            this.userName.Location = new System.Drawing.Point(68, 55);
            this.userName.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.userName.Name = "userName";
            this.userName.Size = new System.Drawing.Size(244, 25);
            this.userName.TabIndex = 0;
            this.userName.TextChanged += new System.EventHandler(this.TextBox1_TextChanged);
            // 
            // password
            // 
            this.password.Location = new System.Drawing.Point(68, 126);
            this.password.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.password.Name = "password";
            this.password.Size = new System.Drawing.Size(244, 25);
            this.password.TabIndex = 3;
            this.password.TextChanged += new System.EventHandler(this.TextBox4_TextChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Stencil", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(64, 28);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(85, 18);
            this.label1.TabIndex = 4;
            this.label1.Text = "Username";
            this.label1.Click += new System.EventHandler(this.Label1_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Stencil", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(64, 100);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(85, 18);
            this.label2.TabIndex = 5;
            this.label2.Text = "PASSWORD";
            // 
            // Submit
            // 
            this.Submit.Font = new System.Drawing.Font("AcmeFont", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Submit.Location = new System.Drawing.Point(356, 55);
            this.Submit.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Submit.Name = "Submit";
            this.Submit.Size = new System.Drawing.Size(250, 100);
            this.Submit.TabIndex = 6;
            this.Submit.Text = "Submit";
            this.Submit.UseVisualStyleBackColor = true;
            this.Submit.Click += new System.EventHandler(this.Button1_Click);
            // 
            // Company1
            // 
            this.Company1.Font = new System.Drawing.Font("Times New Roman", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Company1.FormattingEnabled = true;
            this.Company1.Location = new System.Drawing.Point(68, 250);
            this.Company1.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Company1.Name = "Company1";
            this.Company1.Size = new System.Drawing.Size(613, 274);
            this.Company1.TabIndex = 7;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 17F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1026, 687);
            this.Controls.Add(this.Company1);
            this.Controls.Add(this.Submit);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.password);
            this.Controls.Add(this.userName);
            this.Font = new System.Drawing.Font("Times New Roman", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Name = "Form1";
            this.Text = "Unlist";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox userName;
        private System.Windows.Forms.TextBox password;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button Submit;
        private System.Windows.Forms.CheckedListBox Company1;
    }
}

